from telegrinder import Dispatch, CallbackQuery, Message
from telegrinder.rules import CallbackDataEq, CallbackDataMarkup

dp = Dispatch()

@dp.callback_query(CallbackDataEq("button/1"))
async def handle_press_inline_button(cb: CallbackQuery):
    """
    CallbackQuery.answer отображает сообщение в виде подсказки, а не сообщения
    """
    await cb.answer("Wow, you pressed 'InlineProfile' inline button!")

@dp.callback_query(CallbackDataEq("button/2"))
async def handle_press_inline_button(cb: CallbackQuery):
    """
        CallbackQuery.answer отображает сообщение в виде подсказки, а не сообщения
    """
    await cb.answer("Wow, you pressed 'InlineBalance' inline button!")

@dp.callback_query(CallbackDataEq("button/3"))
async def handle_press_inline_button(message: Message):
    """
        answer отображает сообщение в виде подсказки, а не сообщения
    """
    await message.answer("Wow, you pressed 'InlineExit' inline button!")

@dp.callback_query(CallbackDataMarkup("button/<index:int>"))
async def handle_press_inline_button(cb: CallbackQuery, index: int):
    """
    Здесь обрабатывается сразу все полезные нагрузки с помощью правила CallbackDataMarkup,
    которые указаны при создании клавиатуры.
    Обработчик принимает параметр index типа int, который указан в шаблоне button/<index:int>
    """
    await cb.answer(f"Wow, you pressed '{index}' inline button!")
