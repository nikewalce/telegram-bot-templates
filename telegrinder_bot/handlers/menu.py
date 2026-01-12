from telegrinder import Dispatch, Message
from telegrinder_bot.keyboards.menu import MenuKeyboard, InlineMenuKeyboard
from telegrinder.rules import Command

dp = Dispatch()

@dp.message(Command("menu"))
async def menu(message: Message):
    """
    Метод .get_markup() необходим для того, чтобы объект клавиатуры получить
    в виде объекта ReplyKeyboardMarkup, который ожидает telegram API
    """
    await message.answer(
        "📋 Клавиатура-меню:",
        reply_markup=MenuKeyboard.keyboard.get_markup()
    )

@dp.message(Command("inline_keyboard"))
async def inline_menu(message: Message):
    """
    Метод .get_markup() возвращает инлайн клавиатуру в виде объекта InlineKeyboardMarkup,
    который ожидает telegram API
    """
    await message.answer("Инлайн-клавиатура", reply_markup=InlineMenuKeyboard.inline_keyboard.get_markup())
