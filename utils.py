"""
utils.py

Handles Text-to-Speech generation.
"""

import asyncio
import edge_tts
import os
import uuid


OUTPUT_DIR = "generated_audio"


if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def convert_speed(rate: float) -> str:
    """
    Converts slider value (0.5x - 2.0x)
    into Edge-TTS rate.

    Examples

    1.0 -> +0%
    1.5 -> +50%
    0.7 -> -30%
    """

    percentage = int((rate - 1.0) * 100)

    if percentage >= 0:
        return f"+{percentage}%"

    return f"{percentage}%"


async def generate_tts(
    text,
    voice,
    speed,
    filename,
):

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate=speed,
    )

    await communicate.save(filename)


def text_to_speech(
    text,
    voice,
    speed,
):
    """
    Main function called by Streamlit.
    """

    filename = os.path.join(
        OUTPUT_DIR,
        f"{uuid.uuid4().hex}.mp3"
    )

    asyncio.run(
        generate_tts(
            text=text,
            voice=voice,
            speed=convert_speed(speed),
            filename=filename,
        )
    )

    return filename


def estimate_duration(text):
    """
    Approximate speech duration.
    """

    words = len(text.split())

    minutes = words / 150

    seconds = int(minutes * 60)

    return seconds