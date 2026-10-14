import telebot
from telebot import types
from random import randint

bot = telebot.TeleBot("bot token")

markup = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton("Order")
markup.add(btn1)

markup2 = types.ReplyKeyboardMarkup()
btn2 = types.KeyboardButton("Telegram-bot")
btn3 = types.KeyboardButton("Design")
btn4 = types.KeyboardButton("Python Project")
markup2.row(btn2, btn3, btn4)

nokey = types.ReplyKeyboardRemove()

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(msg.chat.id, "I can make orders with various categories and send them to the worker", reply_markup=markup)
    bot.register_next_step_handler(msg, on_click)

def on_click(msg):
    if msg.text == "Order":
        bot.send_message(msg.chat.id, "Choose a category:", reply_markup=markup2)
        bot.register_next_step_handler(msg, category)

def category(msg):
    if msg.text == "Telegram-bot":
        bot.send_message(msg.chat.id, "Describe your bot.", reply_markup = nokey)
        bot.register_next_step_handler(msg, desc, "Telegram bot")
    elif msg.text == "Design":
        bot.send_message(msg.chat.id, "Describe your design.", reply_markup = nokey)
        bot.register_next_step_handler(msg, desc, "design")
    elif msg.text == "Python Project":
        bot.send_message(msg.chat.id, "Describe your bot.", reply_markup = nokey)
        bot.register_next_step_handler(msg, desc, "Python project")

def desc(msg, categor):
    user = msg.text
    username = msg.from_user.username
    bot.send_message(msg.chat.id, "Your order was sent, please wait for 24-48 hours.", reply_markup=markup)
    bot.send_message(chat_id=group chat id here, text=f"Order from @{username}\n\nCategory: {categor}\nDescription: {user}\n\n")

bot.polling(none_stop = True)
