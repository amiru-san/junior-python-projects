import requests
import telebot
from telebot import types
import io

bot = telebot.TeleBot('my token here :)')

# ввести ссылку
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn = types.KeyboardButton("Ввести ссылку 🔗", style='success')
# донат автору :)
btn3 = types.KeyboardButton("Задонатить", style='primary')
btn4 = types.KeyboardButton("Мой канал", style='danger')

markup.add(btn)
markup.add(btn3)
markup.add(btn4)

# отмена
markup_cancel = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn2 = types.KeyboardButton("Отмена", style='danger')

markup_cancel.add(btn2)

# донат меню
markup_donate = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
donbut = types.KeyboardButton("5 ⭐", style="success")
donbut2 = types.KeyboardButton("10 ⭐ (🔥)", style="success")
donbut3 = types.KeyboardButton("20 ⭐", style="primary")
donbut4 = types.KeyboardButton("50 ⭐", style="primary")
donbut5 = types.KeyboardButton("100 ⭐ (🔥)", style="danger")
donbut6 = types.KeyboardButton("500 ⭐", style="danger")
back = types.KeyboardButton("Отмена")

markup_donate.add(donbut, donbut2)
markup_donate.add(donbut3, donbut4)
markup_donate.add(donbut5, donbut6)
markup_donate.add(back)

# мой канал
linky = "https://t.me/zypax"
markup_channel = types.InlineKeyboardMarkup()
channel_btn = types.InlineKeyboardButton("vlog.py", url=linky, style="success")
markup_channel.add(channel_btn)

# цены
price = [types.LabeledPrice(label="Донат автору", amount=5)]
price2 = [types.LabeledPrice(label="Донат автору", amount=10)]
price3 = [types.LabeledPrice(label="Донат автору", amount=20)]
price4 = [types.LabeledPrice(label="Донат автору", amount=50)]
price5 = [types.LabeledPrice(label="Донат автору", amount=100)]
price6 = [types.LabeledPrice(label="Донат автору", amount=500)]


@bot.message_handler(commands=['start'])
def start(msg):
    user = msg.from_user.first_name
    bot.send_message(msg.chat.id, f"Привет, {user}!\n\n<b>⚙️ Я бот, который может присылать тебе HTML сайта по ссылке.</b>\n\n<i>Нажми на кнопку</i> «<b>Ввести ссылку</b>» <i>чтобы получить HTML.</i>", reply_markup=markup, parse_mode='HTML')
    
@bot.message_handler(func=lambda msg: msg.text == "Ввести ссылку 🔗")
def ask(forlink):
    botmsg = bot.reply_to(forlink, f"Строчка должна содержать «https://» или «http://»\n<b>Ожидание ссылки...</b>", parse_mode='HTML', reply_markup=markup_cancel)
    bot.register_next_step_handler(botmsg, receiver)
    
@bot.message_handler(func=lambda msg: msg.text == "Задонатить")
def donate(msg):
    bot.reply_to(msg, '<b>Выбери сумму:</b>', parse_mode='HTML', reply_markup=markup_donate)
    
@bot.message_handler(func=lambda msg: msg.text == "5 ⭐")
def don1(msg):
    bot.send_invoice(chat_id=msg.chat.id, title="🔥 Поддержка автора", description="Ваши донаты помогат мне монетизировать проект, и дают огромную поддержку в моих будущих проектах :)", invoice_payload="donation_payload_user_{}".format(msg.from_user.id), provider_token="", currency='XTR', prices=price, start_parameter="donate-star")
    
@bot.message_handler(func=lambda msg: msg.text == "10 ⭐ (🔥)")
def don2(msg):
    bot.send_invoice(chat_id=msg.chat.id, title="🔥 Поддержка автора", description="Ваши донаты помогат мне монетизировать проект, и дают огромную поддержку в моих будущих проектах :)",invoice_payload="donation_payload_user_{}".format(msg.from_user.id), provider_token="", currency='XTR', prices=price2, start_parameter="donate-star")

@bot.message_handler(func=lambda msg: msg.text == "20 ⭐")
def don3(msg):
    bot.send_invoice(chat_id=msg.chat.id, title="🔥 Поддержка автора", description="Ваши донаты помогат мне монетизировать проект, и дают огромную поддержку в моих будущих проектах :)", invoice_payload="donation_payload_user_{}".format(msg.from_user.id), provider_token="", currency='XTR', prices=price3, start_parameter="donate-star")

@bot.message_handler(func=lambda msg: msg.text == "50 ⭐")
def don4(msg):
    bot.send_invoice(chat_id=msg.chat.id, title="🔥 Поддержка автора", description="Ваши донаты помогат мне монетизировать проект, и дают огромную поддержку в моих будущих проектах :)", invoice_payload="donation_payload_user_{}".format(msg.from_user.id), provider_token="", currency='XTR', prices=price4, start_parameter="donate-star")

@bot.message_handler(func=lambda msg: msg.text == "100 ⭐ (🔥)")
def don5(msg):
    bot.send_invoice(chat_id=msg.chat.id, title="🔥 Поддержка автора", description="Ваши донаты помогат мне монетизировать проект, и дают огромную поддержку в моих будущих проектах :)", invoice_payload="donation_payload_user_{}".format(msg.from_user.id), provider_token="", currency='XTR', prices=price5, start_parameter="donate-star")

@bot.message_handler(func=lambda msg: msg.text == "500 ⭐")
def don6(msg):
    bot.send_invoice(chat_id=msg.chat.id, title="🔥 Поддержка автора", description="Ваши донаты помогат мне монетизировать проект, и дают огромную поддержку в моих будущих проектах :)", invoice_payload="donation_payload_user_{}".format(msg.from_user.id), provider_token="", currency='XTR', prices=price6, start_parameter="donate-star")

@bot.message_handler(func=lambda msg: msg.text == "Отмена")
def exit(msg):
    bot.send_message(msg.chat.id, "Донат отменён.")
    start(msg)
    return

def receiver(msg):
    link = msg.text
    if link == "Отмена":
        bot.send_message(msg.chat.id, "Действие отменено.")
        start(msg)
        return
    else:
        check = bot.reply_to(msg, f"Проверяю ссылку...")
        bot.send_chat_action(msg.chat.id, 'upload_document')

        if link and ("http://" in link or "https://" in link):
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
            try:
                req = requests.get(link, headers=headers, timeout=5, verify=True)
                req.encoding = req.apparent_encoding or 'utf-8'
            except requests.exceptions.RequestException:
                bot.delete_message(chat_id=msg.chat.id, message_id=check.message_id)
                bot.send_message(msg.chat.id, "Ошибка: сайт заблокировал вход, попробуйте другой сайт.")
                return
        else:
            bot.send_message(msg.chat.id, "Неверный адрес ссылки.")
            start(msg)
            return
        
        if req.status_code == 200:
            html_bytes = req.text.encode('utf-8')
            html_file = io.BytesIO(html_bytes)
            html_file.name = "page.html"
            bot.send_document(msg.chat.id, document=html_file, caption="📎 @HTMLbySitebot")
            start(msg)
            return
    
        elif 300 <=req.status_code < 400:
            bot.send_message(msg.chat.id, "Ошибка: Сайт переехал, нужна его новая ссылка.")
         
        elif 400 <= req.status_code < 500:
             bot.send_message(msg.chat.id, "Ошибка: Неверный адрес или нет прав.")
                    
        elif 500 <= req.status_code < 600:
            bot.send_message(msg.chat.id, "Ошибка: Сломался код сайта или упала база данных.")
    
        else:
            bot.send_message(msg.chat.id, "Произошла неизвестная ошибка, попробуйте отправить другую ссылку.")
            
@bot.message_handler(func=lambda msg: msg.text == "Мой канал")
def channel(msg):
    bot.reply_to(msg, "<b>Мой джуниор/влог канал 👇</b>", parse_mode='HTML', reply_markup=markup_channel)
                
@bot.pre_checkout_query_handler(func=lambda query: True)
def process_pre_checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@bot.message_handler(content_types=['successful_payment'])
def payment_success(message):
    bot.reply_to(
        message, 
        f"Огромное спасибо тебе, благодаря твоему донату, я буду продвигать свои проекты дальше! ❤️"
    )
                
bot.infinity_polling()
