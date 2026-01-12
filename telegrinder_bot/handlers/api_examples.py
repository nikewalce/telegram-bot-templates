from telegrinder import Dispatch, Message
#from telegrinder.kungfu import Ok, Error

dp = Dispatch()

@dp.message()
async def api_handler(message: Message):
    result = await message.api.send_message(
        chat_id=message.chat_id,
        text="Hello via low-level API 👀",
    )

    # match result:
    #     case Error(err):
    #         # контролируем ошибку
    #         print("Telegram API error:", err)
    #         return
    #
    #     case Ok(sent_message):
    #         print("Message sent, id:", sent_message.message_id)
