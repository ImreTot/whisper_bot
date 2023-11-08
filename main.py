import asyncio
import os

from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, Audio
from aiogram.filters.command import CommandStart
import openai

from text import greet_first, greet_second

load_dotenv()

logging.basicConfig(level=logging.INFO)

openai.api_key = os.getenv('WHISPER_TOKEN', 'WHISPER_TOKEN')
BOT_TOKEN = os.getenv('BOT_TOKEN', 'BOT_TOKEN')

router = Router()


async def audio_to_text(file_path: str) -> str:
    """
    Takes a path to an audio file, returns transcribed text.
    """
    with open(file_path, 'rb') as audio_file:
        transcript = await openai.Audio.atranscribe(
	        'whisper-1', audio_file
	    )
    return transcript['text']


async def save_audio_as_mp3(bot: Bot, audio: Audio) -> str:
    """Downloads audio and saves in mp3 format."""
    audio_file_info = await bot.get_file(audio.file_id)
    await bot.download_file(audio_file_info.file_path,
                            f'audio_files/audio-{audio.file_unique_id}.mp3')
    audio_mp3_path = f'audio_files/audio-{audio.file_unique_id}.mp3'
    return audio_mp3_path


@router.message(CommandStart())
async def greet_user(message: Message, bot: Bot) -> None:
    """Greets the user with messages."""
    name = message.from_user.username
    await message.answer(greet_first.format(name=name))
    await message.answer(greet_second)


@router.message(F.content_type == 'audio')
async def process_voice_message(message: Message, bot: Bot) -> None:
    """Принимает все голосовые сообщения и транскрибирует их в текст."""
    audio_path = await save_audio_as_mp3(bot, message.audio)
    transcripted_audio_text = await audio_to_text(audio_path)

    if transcripted_audio_text:
        await message.reply(text=transcripted_audio_text)


async def main() -> None:
    bot: Bot = Bot(token=BOT_TOKEN)
    dp: Dispatcher = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
