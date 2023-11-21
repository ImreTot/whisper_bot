import os

from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
import openai
import logging

import text

logging.basicConfig(level=logging.INFO)

load_dotenv()

API_ID = os.getenv("API_ID", "FAKE_API_ID")
API_HASH = os.getenv("API_HASH", "FAKE_API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN", "FAKE_BOT_TOKEN")
openai.api_key = os.getenv("WHISPER_TOKEN", "FAKE_WHISPER_TOKEN")

app = Client(name="Crowded Room",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)


@app.on_message(filters=filters.audio)
async def process_audio_to_text(client: Client, message: Message):
    """Takes audio and transcribes into text."""
    downloaded_audio = await app.download_media(message)
    with open(downloaded_audio, "rb") as audio:
        transcript = await openai.Audio.atranscribe(
            model="whisper-1", file=audio, response_format="text"
        )
        os.remove(downloaded_audio)
    await client.send_document(chat_id=message.from_user.id,
                               document=transcript)


@app.on_message(
    filters=filters.command(
        [
            "start",
        ]
    )
)
async def greet(client: Client, message: Message) -> None:
    """Greets the user with messages."""
    await message.reply(text.greet_first.format(
        name=message.from_user.username)
    )
    await message.reply(text.greet_second)


app.run()
