import telebot
from telebot import types
from random import choice

lets = "qwertyuiopasdfghjklzxcvbnm@#$&!?1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

bot = telebot.TeleBot('my token here :)')

markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, is_persistent=True)
but = types.KeyboardButton("Сгенерировать Пароль 🔑", style="success")
but2 = types.KeyboardButton("Донат Автору (10 ⭐)", style="primary")
but3 = types.KeyboardButton("Ссылка на мой канал", style="danger")
but4 = types.KeyboardButton("О боте")
markup.row(but)
markup.row(but2, but3, but4)

@bot.message_handler(commands=['start'])
def start(msg):
    user = msg.from_user.first_name
    bot.reply_to(msg, f"Привет, {user}!\n\n🔐 <b>Я бот, который может генерировать 24-х значные пароли.</b>\n\nПросто нажми на кнопку в твоей клавиатуре и я отвечу тебе сгенерированным паролем!", reply_markup=markup, parse_mode='HTML')

@bot.message_handler(func=lambda message: True)
def handle_buttons(msg):
    if msg.text == "Донат Автору (10 ⭐)":
        prices = [types.LabeledPrice(label=" ", amount=10)]
        bot.send_invoice(chat_id=msg.chat.id, title=f"Поддержать автора.",
        description="Студенту на хлебушек...",
        invoice_payload="payload_stars",
        provider_token="", currency = "XTR",
        prices=prices)
    elif msg.text == "Сгенерировать Пароль 🔑":
        passwrd = "".join(choice(lets) for _ in range(24))
        bot.reply_to(msg, f"<b>Нажми, чтобы скопировать:</b>\n\n<code>{passwrd}</code>\n\n🔑 @PasswordGenerationTestBot", parse_mode='HTML')
    elif msg.text == "Ссылка на мой канал":
        bot.reply_to(msg, "<b>Мой джуниор/влог канал: @zypax</b>", parse_mode='HTML')
    elif msg.text == "О боте":
        bot.reply_to(msg, f"<b>⚙️ О боте</b>\n\nБот генерирует случайные «пароли» или «ключи» из букв и знаков, встроенные в код.\n\n<b>❗ Бот не собирает данные или сохраняет пароли.</b>\n\n<blockquote>• Юзернейм Бота: @PasswordGenerationTestBot\n\n• Имя Бота: Генератор Паролей 🔑\n\n• Бот был выпущен 28 августа, 2026 г.</blockquote>", parse_mode="HTML")
        
    
@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout_handler(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@bot.message_handler(content_types=['successful_payment'])
def success_payment_handler(message):
    payment_info = message.successful_payment
    bot.reply_to(
        message, 
        "<b>Спасибо за поддержку! ❤</b>️", parse_mode="HTML")

bot.infinity_polling()