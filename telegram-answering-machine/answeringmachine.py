import telebot
import time

bot = telebot.TeleBot('')

sec = 60

uss = {}

@bot.business_message_handler(func=lambda msg: True)
def greet(msg):
    user = msg.from_user.id
    current_t = time.time()
    
    if user in uss:
        time_passed = current_t - uss[user]
        if time_passed < sec:
            return
    uss[user] = current_t   
    bot.send_message(chat_id=msg.chat.id, text="<b>Здравствуйте, на связи автоответчик 🟢</b>\n\nВаш собеседник сейчас занят, и как только он увидит ваше сообщение, обязательно ответит.\n\n<i>Автоответчик был сделан @pysoh</i>", parse_mode='HTML', business_connection_id=msg.business_connection_id)
    

bot.infinity_polling()