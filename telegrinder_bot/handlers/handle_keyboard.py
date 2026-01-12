from telegrinder import Dispatch, Message
from telegrinder.rules import Text
from telegrinder_bot.keyboards.menu import MenuKeyboard

dp = Dispatch()

"""
Обработчик нажатия кнопок из Keyboard
"""

@dp.message(Text("Profile"))
async def handle_press_button_profile(message: Message):
    await message.answer("Wow, you pressed the 'Profile' button!")

@dp.message(Text("Balance"))
async def handle_press_button_balance(message: Message):
    await message.answer("Wow, you pressed the 'Balance' button!")

@dp.message(Text("Exit"))
async def exit_handler(message: Message):
    await message.answer(
        "Bye 👋",
        reply_markup=MenuKeyboard.keyboard.get_keyboard_remove()
    )