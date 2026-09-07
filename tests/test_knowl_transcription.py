import io
import unittest
import wave
from unittest.mock import patch
from scripts.knowl_transcription import transcribe_recording, MAX_UPLOAD


class TranscriptionTests(unittest.TestCase):
    def test_rejects_empty_and_oversized_uploads(self):
        for audio in (b'', b'x' * (MAX_UPLOAD + 1)):
            with self.assertRaises(ValueError):
                transcribe_recording(audio)

    def test_invalid_audio_never_reaches_model(self):
        with patch('scripts.knowl_transcription.socket.socket') as client:
            with self.assertRaises(ValueError):
                transcribe_recording(b'not audio')
            client.assert_not_called()

    def test_duration_limit_before_model(self):
        stream = io.BytesIO()
        with wave.open(stream, 'wb') as wav:
            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(16000)
            wav.writeframes(b'\0' * (31 * 32000))
        with patch('scripts.knowl_transcription.socket.socket') as client:
            with self.assertRaisesRegex(ValueError, '30 seconds'):
                transcribe_recording(stream.getvalue())
            client.assert_not_called()
