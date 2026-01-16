from telegram import LabeledPrice, ShippingOption, Update
from telegram.ext import (
    ContextTypes,
)
# Insert the token from your payment provider.
# In order to get a provider_token see https://core.telegram.org/bots/payments#getting-a-token
PAYMENT_PROVIDER_TOKEN = "PAYMENT_PROVIDER_TOKEN"

async def start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет инструкцию пользователю:
        /shipping — оплата с доставкой
        /noshipping — оплата без доставки
        """
    msg = (
        "Use /shipping to receive an invoice with shipping included, or /noshipping for an "
        "invoice without shipping."
    )
    await update.message.reply_text(msg)

async def start_with_shipping_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Формирует счёт (invoice)
    Запрашивает имя, телефон, email и адрес доставки
    Включает гибкую доставку (is_flexible=True)
    Отправляет счёт пользователю
    """
    chat_id = update.message.chat_id
    title = "Payment Example"
    description = "Example of a payment process using the python-telegram-bot library."
    # Unique payload to identify this payment request as being from your bot
    payload = "Custom-Payload"
    # Set up the currency.
    # List of supported currencies: https://core.telegram.org/bots/payments#supported-currencies
    currency = "USD"
    # Price in dollars
    price = 1
    # Convert price to cents from dollars.
    prices = [LabeledPrice("Test", price * 100)]
    # Optional parameters like need_shipping_address and is_flexible trigger extra user prompts
    # https://docs.python-telegram-bot.org/en/stable/telegram.bot.html#telegram.Bot.send_invoice
    await context.bot.send_invoice(
        chat_id,
        title,
        description,
        payload,
        currency,
        prices,
        provider_token=PAYMENT_PROVIDER_TOKEN,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=True,
        is_flexible=True,
    )

async def start_without_shipping_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """
    Формирует счёт без запроса адреса
    Используется для цифровых товаров / услуг
    """
    chat_id = update.message.chat_id
    title = "Payment Example"
    description = "Example of a payment process using the python-telegram-bot library."
    # Unique payload to identify this payment request as being from your bot
    payload = "Custom-Payload"
    currency = "USD"
    # Price in dollars
    price = 1
    # Convert price to cents from dollars.
    prices = [LabeledPrice("Test", price * 100)]

    # optionally pass need_name=True, need_phone_number=True,
    # need_email=True, need_shipping_address=True, is_flexible=True
    await context.bot.send_invoice(
        chat_id,
        title,
        description,
        payload,
        currency,
        prices,
        provider_token=PAYMENT_PROVIDER_TOKEN,
    )

async def shipping_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Проверяет, что платёж создан этим ботом
    Предлагает варианты доставки
    Возвращает список доступных способов доставки и цен
    """
    query = update.shipping_query
    # Verify if the payload matches, ensure it's from your bot
    if query.invoice_payload != "Custom-Payload":
        # If not, respond with an error
        await query.answer(ok=False, error_message="Something went wrong...")
        return

    # Define available shipping options
    # First option with a single price entry
    options = [ShippingOption("1", "Shipping Option A", [LabeledPrice("A", 100)])]
    # Second option with multiple price entries
    price_list = [LabeledPrice("B1", 150), LabeledPrice("B2", 200)]
    options.append(ShippingOption("2", "Shipping Option B", price_list))
    await query.answer(ok=True, shipping_options=options)

# After (optional) shipping, process the pre-checkout step
async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Telegram запрашивает подтверждение перед списанием денег
    Бот обязан ответить ok=True
    Иначе платёж будет отменён
    """
    query = update.pre_checkout_query
    # Verify if the payload matches, ensure it's from your bot
    if query.invoice_payload != "Custom-Payload":
        # If not, respond with an error
        await query.answer(ok=False, error_message="Something went wrong...")
    else:
        await query.answer(ok=True)

# Final callback after successful payment
async def successful_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Срабатывает после успешной оплаты
    Благодарит пользователя
    """
    await update.message.reply_text("Thank you for your payment.")
