from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Каталог")],
        [KeyboardButton(text="Корзина")],
        [KeyboardButton(text="FAQ")]])

catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Games", callback_data="games")],
        [InlineKeyboardButton(text="Movies", callback_data="movies")],
        [InlineKeyboardButton(text="Songs", callback_data="songs")],
    ]
)
