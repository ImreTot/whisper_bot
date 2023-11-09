import os

from pyrogram import Client
from dotenv import load_dotenv
import openai
import logging

logging.basicConfig(level=logging.INFO)

load_dotenv()

API_ID = os.getenv('API_ID', 'FAKE_API_ID')
API_HASH = os.getenv('API_HASH', 'FAKE_API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN', 'BOT_TOKEN')
openai.api_key = os.getenv('WHISPER_TOKEN', 'WHISPER_TOKEN')

app = Client(name='Crowded Room',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)

app.run()
