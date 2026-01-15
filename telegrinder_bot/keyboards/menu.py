from telegrinder.tools.keyboard import Button, Keyboard

#https://github.com/timoniq/telegrinder/blob/dev/docs/tutorial/ru/7_keyboard.md

class MenuKeyboard:
    """
        Клавиатура-меню
    """
    PROFILE = Button("Profile")
    BALANCE = Button("Balance")
    EXIT = Button("Exit")

    keyboard = (
        Keyboard()
        .add(PROFILE)
        .add(BALANCE)
        .row()
        .add(EXIT)
    )

from telegrinder.tools.keyboard import InlineButton, InlineKeyboard
class InlineMenuKeyboard:
    """
    Inline клавиатура (кнопки в сообщении)

    Полезная нагрузка может быть одной из нескольких типов:
    str
    dict
    dataclasses.dataclass
    msgspec.Struct

    import dataclasses
    import msgspec


    @dataclasses.dataclass
    class Item:
        name: str
        amount: int

    class Point(msgspec.Struct):
        x: int
        y: int


    inline_keyboard = (
        InlineKeyboard()
        .add(InlineButton("apple", callback_data=Item("apple", 5)))
        .add(InlineButton("point", callback_data=Point(2, 2)))
        .add(InlineButton("dict", callback_data=dict(key="value")))
    )
    """
    PROFILE = Button("InlineProfile")
    BALANCE = Button("InlineBalance")
    EXIT = Button("InlineExit")

    inline_keyboard = (
        InlineKeyboard()
        .add(InlineButton("InlineProfile", callback_data="button/1"))
        .add(InlineButton("InlineBalance", callback_data="button/2"))
        .row()
        .add(InlineButton("InlineExit", callback_data="button/3"))
    )
