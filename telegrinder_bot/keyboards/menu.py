from telegrinder.tools.keyboard import Button, Keyboard

class MenuKeyboard:
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
