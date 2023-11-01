from aiogram import F, Router, types
from aiogram.filters.command import Command

import keyboard
import text

router = Router()


@router.message(Command('start'))
async def start_handler(msg: types.Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name),
                     reply_markup=keyboard.menu)


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: types.Message) -> None:
    await msg.answer(text.menu, reply_markup=keyboard.menu)
