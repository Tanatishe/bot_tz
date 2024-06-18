from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

router = Router()


  
@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer('Menu:', reply_markup=kb.main)


@router.message(F.text)
async def callback_catalog(message:Message):
    if message.text == 'Каталог':
        await message.answer('Catalog:', reply_markup=kb.catalog)
    elif message.text == 'Корзина':
        await message.answer('BASKET')        
    elif message.text == 'FAQ':
        await message.answer('FAQ FOR U')
    else:
        await message.answer('neponyatno')
    



