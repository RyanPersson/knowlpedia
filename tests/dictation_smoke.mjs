import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {chromium} from 'playwright';
const base=process.env.PREVIEW_URL || 'http://127.0.0.1:8012';
const token=(await readFile('.preview-server/codex-access-token','utf8')).trim();
const browser=await chromium.launch({headless:true,args:['--use-fake-ui-for-media-stream','--use-fake-device-for-media-stream',`--use-file-for-fake-audio-capture=${process.cwd()}/tmp/dictation-test/speech.wav`]});
try {
 const page=await browser.newPage();
 await page.addInitScript(token=>localStorage.setItem('knowl-codex-access-key',token),token);
 const rejected=await page.request.post(base+'/__knowlpedia/transcribe',{data:'bad'});
 assert.equal(rejected.status(),401);
 await page.goto(base+'/conversation/');
 await page.getByLabel('Your message').fill('Draft:');
 await page.getByRole('button',{name:'Dictate',exact:true}).click();
 await page.getByRole('button',{name:'Stop recording'}).waitFor();
 await page.waitForTimeout(4000);
 await page.getByRole('button',{name:'Stop recording'}).click();
 await page.waitForFunction(()=>document.getElementById('voice-status').textContent==='Review your transcript, then send.',{},{timeout:90000});
 const text=await page.getByLabel('Your message').inputValue();
 assert.match(text,/Draft:.*local microphone transcription test/i);
 assert.equal(await page.getByRole('button',{name:'Send to Codex',exact:true}).isEnabled(),true);
 await page.evaluate(()=>localStorage.setItem('knowl-theme','dark'));
 await page.reload();
 await page.setViewportSize({width:390,height:1000});
 await page.screenshot({path:'tmp/dictation-test/dark-mobile.png'});
 assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
 console.log('Real browser recording → shared Parakeet → editable draft passed; dark mobile layout fits.');
}finally{await browser.close();}
