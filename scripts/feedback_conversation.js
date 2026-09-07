'use strict';
const $ = id => document.getElementById(id);
const tokenKey = 'knowl-codex-access-key';
try { $('key').value = localStorage.getItem(tokenKey) || ''; } catch {}
$('knowl').value = new URLSearchParams(location.search).get('knowlId') || '';
let sending = false;
async function api(path, body) {
  const token = $('key').value.trim();
  if (!token) throw Error('Enter your preview access key first.');
  const response = await fetch(path, {cache:'no-store', method:body ? 'POST' : 'GET', headers:{Authorization:`Bearer ${token}`, 'Content-Type':'application/json'}, ...(body ? {body:JSON.stringify(body)} : {})});
  const data = await response.json();
  if (!response.ok) throw Error(data.error || 'The request failed.');
  try { localStorage.setItem(tokenKey, token); } catch {}
  return data;
}
let previous = '';
async function refresh() {
  const data = await api('/__knowlpedia/conversation');
  const serialized = JSON.stringify(data.messages);
  if (serialized !== previous) {
    const history = $('history');
    const atBottom = history.scrollHeight - history.scrollTop - history.clientHeight < 80;
    history.replaceChildren();
    for (const message of data.messages) {
      const article = document.createElement('article');
      article.dataset.role = message.role;
      const label = document.createElement('strong');
      label.textContent = message.role === 'user' ? 'You' : 'Codex';
      article.append(label);
      if (message.context) {
        const context = document.createElement('p'); context.className='context'; context.textContent=message.context; article.append(context);
      }
      const body = document.createElement('div'); body.className='message'; body.textContent=message.text; article.append(body);
      history.append(article);
    }
    if (!data.messages.length) history.textContent='No messages yet.';
    if (atBottom || !previous) history.scrollTop=history.scrollHeight;
    previous=serialized;
  }
  if (!sending) $('status').textContent = data.active ? 'Codex is working…' : `${data.messages.length} messages · conversation loaded`;
}
$('refresh').onclick = () => refresh().catch(e => {$('status').textContent=e.message;});
$('latest').onclick = () => {$('history').scrollTop=$('history').scrollHeight;};
$('compose').onsubmit = async event => {
  event.preventDefault(); if (sending) return;
  const message=$('message').value.trim(), knowlId=$('knowl').value.trim(), intent='auto';
  if (!message) return;

  sending=true; $('send').disabled=true; $('dictate').disabled=true; $('status').textContent='Sending…';
  try {
    const job=await api('/__knowlpedia/codex',{intent,knowlId,message,conversation:true,url:location.href});
    $('message').value='';
    let result;
    do {
      await new Promise(resolve=>setTimeout(resolve,1500));
      result=await api(`/__knowlpedia/codex/${encodeURIComponent(job.jobId)}`);
      $('status').textContent=result.status==='queued' ? 'Queued…' : 'Codex is working…';
      await refresh();
    } while (['queued','running'].includes(result.status));
    if (result.status!=='completed') throw Error(result.error || `Codex stopped: ${result.status}`);
    $('status').textContent='Codex replied.';
  } catch(e) { $('status').textContent=e.message; }
  finally {sending=false; $('send').disabled=false; $('dictate').disabled=!navigator.mediaDevices?.getUserMedia || !window.MediaRecorder || !window.isSecureContext;}
};
let recorder=null, stream=null, recordTimer=null, leaving=false;
const stopTracks=()=>{if(stream) stream.getTracks().forEach(track=>track.stop());stream=null;};
if (!navigator.mediaDevices?.getUserMedia || !window.MediaRecorder || !window.isSecureContext) {
  $('dictate').disabled=true;
  $('voice-note').textContent='Open the HTTPS preview to use the microphone. Device keyboard dictation also works in the message box.';
} else {
  $('dictate').onclick=async()=>{
    if(sending) return;
    if(!$('key').value.trim()) {$('voice-status').textContent='Enter your preview access key first.';return;}
    if(recorder?.state==='recording') {recorder.stop();return;}
    $('dictate').disabled=true; $('send').disabled=true;
    try {
      stream=await navigator.mediaDevices.getUserMedia({audio:true});
      const mimeType=['audio/webm;codecs=opus','audio/ogg;codecs=opus','audio/mp4'].find(type=>MediaRecorder.isTypeSupported(type));
      recorder=new MediaRecorder(stream,mimeType?{mimeType}:undefined);
      const chunks=[];
      recorder.ondataavailable=event=>{if(event.data.size) chunks.push(event.data);};
      recorder.onerror=()=>{$('voice-status').textContent='Recording failed. Try again.';clearTimeout(recordTimer);stopTracks();$('dictate').disabled=false;$('send').disabled=false;};
      recorder.onstop=async()=>{
        clearTimeout(recordTimer); stopTracks(); $('dictate').disabled=true;
        $('dictate').textContent='Dictate';
        if(leaving) return;
        $('voice-status').textContent='Transcribing on the OptiPlex…';
        try {
          const token=$('key').value.trim();
          if(!token) throw Error('Enter your preview access key first.');
          const response=await fetch('/__knowlpedia/transcribe', {
            method:'POST', headers:{Authorization:`Bearer ${token}`}, body:new Blob(chunks,{type:recorder.mimeType}),
          });
          const result=await response.json();
          if(!response.ok) throw Error(result.error || 'Transcription failed.');
          $('message').value+=($('message').value && result.text ? ' ' : '')+result.text;
          $('voice-status').textContent=result.text ? 'Review your transcript, then send.' : 'No speech recognized. Try again.';
          $('message').focus();
        }catch(error){$('voice-status').textContent=error.message;}
        finally{$('dictate').disabled=false;$('send').disabled=sending;}
      };
      recorder.start();
      $('dictate').textContent='Stop recording'; $('dictate').disabled=false;
      $('voice-status').textContent='Recording… stops automatically after 29 seconds.';
      recordTimer=setTimeout(()=>{if(recorder.state==='recording') recorder.stop();},29000);
    }catch(error){stopTracks();$('dictate').disabled=false;$('send').disabled=sending;$('voice-status').textContent=`Microphone unavailable: ${error.message}`;}
  };
  window.addEventListener('pagehide',()=>{leaving=true;clearTimeout(recordTimer);if(recorder?.state==='recording') recorder.stop();stopTracks();});
}
const scheme=matchMedia('(prefers-color-scheme: dark)');
function applyConversationTheme() {
  let theme;
  try{theme=localStorage.getItem('knowl-theme');}catch{}
  if(!['light','dark'].includes(theme)) theme=scheme.matches?'dark':'light';
  document.documentElement.dataset.theme=theme;
  $('theme-toggle').textContent=theme==='dark'?'Use light theme':'Use dark theme';
}
$('theme-toggle').onclick=()=>{
  const next=document.documentElement.dataset.theme==='dark'?'light':'dark';
  try{localStorage.setItem('knowl-theme',next);}catch{}
  document.documentElement.dataset.theme=next;
  $('theme-toggle').textContent=next==='dark'?'Use light theme':'Use dark theme';
};
scheme.addEventListener('change',applyConversationTheme);
window.addEventListener('storage',event=>{if(event.key==='knowl-theme') applyConversationTheme();});
applyConversationTheme();
if($('key').value) $('refresh').click();
setInterval(()=>{if(!document.hidden && !sending && $('key').value) refresh().catch(e=>{$('status').textContent=e.message;});},5000);
