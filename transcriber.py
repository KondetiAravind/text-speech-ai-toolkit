"""
transcriber.py

Speech-to-Text using Faster Whisper.
"""

from faster_whisper import WhisperModel


print("Loading Whisper Model...")


model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8",
)

print("Whisper Loaded Successfully.")


def speech_to_text(audio_path):

    segments, info = model.transcribe(
        audio_path,
        beam_size=5,
    )

    transcript = ""

    for segment in segments:
        transcript += segment.text + " "

    return transcript.strip()