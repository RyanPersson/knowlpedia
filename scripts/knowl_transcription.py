"""Decode browser recordings in memory and use Oreo's shared Parakeet model."""
import json
import socket
import struct
import subprocess

MAX_UPLOAD = 5 * 1024 * 1024
MAX_PCM = 30 * 16000 * 2


def transcribe_recording(recording: bytes, socket_path='/run/oreo-parakeet/requests.sock') -> str:
    if not 0 < len(recording) <= MAX_UPLOAD:
        raise ValueError('Recording is empty or exceeds 5 MB.')
    decoded = subprocess.run([
        'ffmpeg', '-nostdin', '-v', 'error', '-protocol_whitelist', 'pipe',
        '-format_whitelist', 'matroska,webm,mov,ogg,wav', '-i', 'pipe:0',
        '-t', '31', '-vn', '-ac', '1', '-ar', '16000', '-f', 's16le', 'pipe:1',
    ], input=recording, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15)
    pcm = decoded.stdout
    if decoded.returncode or not pcm:
        raise ValueError('Could not decode this audio recording.')
    if len(pcm) > MAX_PCM:
        raise ValueError('Recordings must be 30 seconds or shorter.')
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
        client.settimeout(120)
        client.connect(socket_path)
        client.sendall(struct.pack('!I', len(pcm)) + pcm)
        data = bytearray()
        while len(data) <= 65536:
            chunk = client.recv(4096)
            if not chunk:
                break
            data.extend(chunk)
            if b'\n' in chunk:
                break
        result = json.loads(data)
    if 'error' in result:
        raise ValueError(result['error'])
    return result['text']
