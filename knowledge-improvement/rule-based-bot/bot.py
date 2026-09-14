# I'm lazy to translate the code through english cuz my main language is russian, i hope you understand :_)

import random
import re
import time
import difflib
import json
import requests
import os

#блок матов
def is_fully_profane(text):
    t = text.lower()
    leet_map = {
        '1': 'i', '!': 'i', '¹': 'i', '¡': 'i', '|': 'i',
        '0': 'o', '@': 'a', '4': 'a', '$': 's', '5': 's', 
        '3': 'e', '7': 't', '+': 't', '8': 'b', '9': 'g'
    }
    for bad_char, good_char in leet_map.items():
        t = t.replace(bad_char, good_char)
    t = re.sub(r'[^a-z]', '', t)
    t = re.sub(r'(.)\1+', r'\1', t)
    bad_words = [
        "shit", "fuck", "bitch", "ass", "cunt", 
        "dick", "pussy", "whore", "bastard", "sex" "penis"
    ]
    for word in bad_words:
        if word in t:
            return True
            
    return False

# настройка json
JSON_PATH = "memory.json"

def load_user_data():
    if os.path.exists(JSON_PATH):
        try:
            with open(JSON_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return {}
    return {}

def save_user_data(data):
    with open(JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


#настройка реквестов
def get_region():
    try:
        response = requests.get("http://ip-api.com/json/", timeout=3).json()
        region = response.get("city", "Unknown")
        return region
    except Exception:
        return "Unknown"
        
#бот
bot_info_commands = [
    "info",
    "bot",
    "bot info",
    "id"
]

bot_desc = [
    "== I am here, coffee's brewing. ==",
    "== New day, new vibe. Let's get it! ==",
    "== Your favorite digital bestie is online. ==",
    "== Sending you good vibes today! ==",
    "== I've got your back, no matter what. ==",
    "== Let's crush this day together! ==",
    "== I am here. What's the plan? ==",
    "== Always here whenever you wanna chat. ==",
    "== Quick chats, big support, zero judgment. ==",
    "== Coffee's ready, just waiting on you. ==",
    "== Your virtual soulmate is in the house. ==",
    "== Let's make today fun and productive. ==",
    "== Sorting out your chaos in style. ==",
    "== Here to save your time and sanity. ==",
    "== New goals? We've got this! ==",
    "== Need to vent or need a hand? I'm here. ==",
    "== Keeping things simple and stress-free. ==",
    "== Your ultimate partner-in-crime is ready. ==",
    "== You and me? The perfect team. ==",
    "== I am here! What are we doing first? ==",
    "== I am always here when you need a friend. ==",
    "== Only good vibes and warm replies. ==",
    "== Your go-to girl for literal fun. ==",
    "== Bringing some cozy vibes to your day. ==",
    "== I am ready. Let's begin! ==",
    "== Forget the stress, let's focus on you. ==",
    "== Your ride-or-die digital friend. ==",
    "== New look, same me, ready to hype you up. ==",
    "== I'll handle the boring stuff. You relax. ==",
    "== I'm here for you, always. =="
]

# ответы бота чееек

# приветствие
bot_greet = [
    "Hello {name}. I am here.",
    "Hi {name}. I'm ready when you are.",
    "Hello {name}. Glad you could make it.",
    "Hi there, {name}. Let's get started.",
    "Hello {name}. I've been waiting for you.",
    "Hi {name}. I'm ready to discuss whatever you need.",
    "Hello {name}. I'm entirely at your disposal.",
    "Hi {name}. Have a seat.",
    "Hello {name}. Tell me what's on your mind.",
    "Hi {name}. I'm here and I'm listening.",
    "Hello {name}. Let's get straight to business.",
    "Hi {name}. I hope your day is going productively.",
    "Hello {name}. I'm ready to give you my full attention.",
    "Hi {name}. I appreciate you taking the time.",
    "Hello {name}. We definitely have things to talk about"
]

# прощание досвидос
bot_byes = [
    "Goodbye {name}, and take care of yourself.",
    "Got it {name}. Let's talk again next time you're free.",
    "Understood perfectly, {name}. I'll be logging off and closing the session too.",
    "Copy that {name}. See you around next time.",
    "Roger that, {name}. Thanks for letting me know. Disconnecting right now.",
    "I hear you, {name}. No problem at all. Taking my leave and heading out now.",
    "Clear, {name}. Thanks for the update. I am going offline from here.",
    "Message received loud and clear from you, {name}. Goodbye and have a great rest of the day.",
    "Understood, {name}. That's completely fine. See you later, take care.",
    "Got it, {name}. Appreciate the heads up. Have a truly wonderful day ahead.",
    "Copy that, {name}. Have a highly productive rest of your day today.",
    "Roger that, {name}. Everything makes sense. Talk soon and stay safe.",
    "Fair enough, {name}. Let's leave it at that for now. Goodbye.",
    "Understood, {name}. Wish you all the best. Goodbye and take it easy."
]

# благодарность ботка
bot_thank = [
    "You are very welcome {name}. Wishing you a good time.",
    "It was my absolute pleasure for you, {name}. Have a fantastic time.",
    "You are most welcome, {name}. I am glad I could make things easier for you.",
    "Always at your service, {name}. Have a great rest of your time.",
    "Thank you for your kind words, {name}. I truly appreciate it.",
    "You're very welcome, {name}. Wishing you all the best with your tasks or work.",
    "The pleasure is all mine, {name}. Have a wonderful and productive day.",
    "Not a problem at all for you, {name}. Glad to hear that.",
    "It's always a pleasure, {name}. Have a beautiful day!",
    "You are very welcome, {name}. Take care and have a wonderful week.",
    "The pleasure is entirely mine, {name}. Enjoy the rest of your day."
]

# регион/локация
region_bot = [
    "Your current system location is set to {region}, {name}.",
    "According to my network protocols, you are running from {region}.",
    "Checking your server coordinates... It says {region}.",
    "Current location data received: {region}.",
    "We are currently connected through {region} right now!"
]


# непонятка
bot_misund = [
    "Sorry, I didn't get that. Could you rephrase it?",
    "I'm not sure I understand. Could you put it differently?",
    "Fix that, please. I didn't quite catch your meaning.",
    "I'm confused. Rephrase that for me, will you?",
    "Could you change the wording? I didn't follow.",
    "Sorry, I didn't understand. Try explaining it another way.",
    "Correction needed, I didn't get what you meant.",
    "I lost the thread. Could you rephrase your point?",
    "Sorry, that didn't make sense to me. Try rephrasing it.",
    "I'm having trouble understanding. Mind putting it another way?",
    "Could you clarify that? I didn't process it correctly.",
    "Sorry, I didn't follow. Rephrase that for me.",
    "I'm not entirely sure what you mean. Could you reword that?",
    "Fix that sentence, I didn't quite understand.",
    "Sorry, I missed your point. Try stating it differently."
]

# приветствия пользователя
greet = [
    "hi",
    "hai",
    "hello",
    "hey",
    "yo",
    "sup",
    "greetings",
    "hiya",
    "heya",
    "hey there",
    "whatsup",
    "wazzup",
    "wassup",
    "hallo",
    "welcome",
    "cheers",
    "wsg"
]

#досвидания пользователя
byes = [
    "bye",
    "later",
    "cya",
    "leaving",
    "gtg",
    "bai"
]

# благодарность от пользователя
thanks = [
    "ty",
    "thx",
    "appreciate it",
    "thank you",
    "thanks",
    "cheers"
]

#регион/локация от пользователя
locate = {
    "region": "location",
    "location": "location",
    "city": "location",
    "country": "location",
    "coordinates": "location",
    "position": "location",
    "zone": "location"
}

# закрытие какой-либо функции
close = [
    "close",
    "exit",
    "remove",
    "leave"
]

# калькулятор ураааа
calc_opener = [
    "calculator",
    "calc",
    "open calculator"
]

divide_error = [
    "Sorry, but division by zero is mathematically impossible.",
    "An error occurred: you cannot divide a number by zero.",
    "Operation denied. Zero is not a valid divisor.",
    "Unfortunately, this calculation cannot be performed with a zero denominator.",
    "Nice try, but division by zero is not allowed.",
    "Sorry, but you can't share something with nobody.",
    "Error: Please choose a number other than zero to divide by.",
    "Action blocked: Attempted to divide by zero.",
    "Sorry, but dividing by zero would break the universe.",
    "Sorry, but my calculator refuses to destroy reality by dividing by zero.",
    "Nice try, but I’m not risking a black hole for your math homework.",
    "You can't divide by zero. Somewhere, a math teacher is crying."
]

digits_error = [
    "Error: Please use numbers only, not letters.",
    "Operation denied. Only numeric values are allowed here.",
    "Unfortunately, letters won't work — I need digits only.",
    "Nice attempt, but this calculation requires strictly numbers.",
    "Please type using numbers only. Save the letters for your texts.",
    "Input error: We only speak the language of numbers here.",
    "Action blocked: Text detected where only digits should be.",
    "Nice try, but I only understand the language of mathematics.",
    "Error: Letters are powerless here, please enter numbers only.",
    "Unfortunately, you can't do math with words. I need digits.",
    "Please use digits. Somewhere, a math teacher is crying because you used letters.",
    "Input rejected. My calculator refuses to read text; it skipped literature class."
]


def calc():
        print("=== CALCULATOR ===")
        while True:
            try:
                # первый ввод
                first_input = input("First Number: ")
            
                if first_input.lower() in close:
                    print(bot_name, "Successfully Closed.")
                    break
                
                calcul_user = float(first_input)
                #,второй ввод
                second_input = input("Second Number: ")
            
                if second_input.lower() in close:
                    print(bot_name, "Successfully Closed.")
                    break
                
                calcul_user2 = float(second_input)
            
                # решение
                solve = input("Solution (+, -, *, /): ")
            
                if solve == "+":
                    print(bot_name, calcul_user + calcul_user2)
                elif solve == "-":
                    print(bot_name, calcul_user - calcul_user2)
                elif solve == "*":
                    print(bot_name, calcul_user * calcul_user2)
                elif solve == "/":
                    print(bot_name, calcul_user / calcul_user2)
                elif solve in close:
                    print(bot_name, "Successfully Closed.")
                    break
                else:
                    print(bot_name, "Error: Invalid operator.")
                    continue
            except ValueError:
                print(bot_name, random.choice(digits_error))
            except ZeroDivisionError:
               print(bot_name, random.choice(divide_error))
               
# победа, поражение, ничья
win = [
    "Alright, you got me. You win!",
    "I admit it, I lost this one.",
    "Fair play, you totally beat me!",
    "Wow, nice move! You win!",
    "Okay, okay, I surrender. Your victory!",
    "You outsmarted me. Congrats!",
    "No excuses, you won fair and square.",
    "I completely missed that. You win!",
    "Fine, the victory is yours this time.",
    "Victory goes to the human. Well played!"
]

lost = [
    "I won this round, but you did great! Keep it up!",
    "Got you! Close one though, you're playing really well.",
    "My point, but honestly, you're a tough opponent!",
    "I took this one, but that was a really good try.",
    "Got lucky this time! You're doing awesome, let's continue.",
    "This round is mine, but don't give up, you're doing great!",
    "I win here, but you put up a really good fight!",
    "Got you this time! But seriously, you're doing amazing.",
    "My win, but that was an excellent effort. Good job!",
    "I took the point, but you're still doing great. Next round?"
]

tie = [
    "It's a tie. Both sides made the right move.",
    "A draw. We analyzed the situation identically.",
    "It's a tie. Neither of us left any room for error.",
    "We chose the same option. The round is a draw.",
    "No advantage gained. It's a tie, well played.",
    "A perfect match. Neither strategy could overcome the other.",
    "It's a draw. We are completely balanced this round.",
    "The results are identical. It is a tie.",
    "No winner this time. Both choices neutralized each other.",
    "A tie. An equal and well-calculated response from both sides."
]
               
               
# игра-рандомайзер с числом
def randomizer():
    print("=== RANDOMIZER ===")
    while True:
        limit = 2
        bot_guess = random.randint(1, 10)
        user_guess = input("Guess the number from 1 to 10: ").strip()
        if any(char in unsup_rus for char in user_guess):
            print("We are sorry, but this kind of symbols is not supported.")
            continue
        if user_guess.lower() in close:
                    print(bot_name, "Successfully Closed.")
                    break
        user_guess = user_guess.translate(str.maketrans("", "", signs))
        
        if not user_guess.isdigit():
            print("Use only numbers.")
            continue
        elif len(user_guess) > limit:
            print("There must be at least 1 or 2 numbers.")
            continue
        user_guess = int(user_guess)
        
        if user_guess == bot_guess:
            print(bot_name, "My number is ", bot_guess)
            print(bot_name, random.choice(win))
        else:
            print(bot_name, "My number is ", bot_guess)
            print(bot_name, random.choice(lost))
# слова для акцивации рандомайзера
user_randomizer = [
    "randomizer",
    "random"
]

# 
time_keys = {
    "time": "timer",
    "hour": "hours",
    "minute": "minutes",
    "mins": "minutes",
    "date": "dater",
    "clock": "timer",
    "day": "week_day",
    "year": "years",
    "month": "months"
}

# time
time_bot = [
    "According to my clock, it's {hour}:{minute:02d}.",
    "Right now it's {hour}:{minute:02d}.",
    "The clock says {hour}:{minute:02d}.",
    "It's {hour}:{minute:02d} right now."
]
# hours
hour_bot = [
    "It's currently the {hour} o'clock hour.",
    "We are inside the {hour} hour right now.",
    "The hour counter is at {hour}.",
    "It's {hour} o'clock sharp. Well, almost sharp..."
]
# minute
minute_bot = [
    "The minute hand is currently at {minute}.",
    "It's exactly {minute} minutes past the hour.",
    "We are {minute} minutes into this hour, {name}.",
    "My counter shows {minute} minutes right now."
]
# date
date_bot = [
    "Today is {day}/{month}/{year} (DD/MM/YYYY).",
    "According to my calendar, it's {day}/{month}/{year}, {name}.",
    "It's {day}/{month}/{year}. Can you believe we are already in {year}?",
    "Today's date is {day}/{month}/{year}."
]
# days
day_bot = [
    "Today is {week}, {name}.",
    "According to my calendar, it's {week}.",
    "It's {week} today, {name}.",
    "My clock says it's {week}."
]
# age
year_bot = [
    "We are currently in the year {year}, {name}.",
    "According to my calendar, it's {year}.",
    "It's {year} right now.",
    "The current year is {year}, {name}."
]
# month
month_bot = [
    "We are currently in {month}, {name}.",
    "According to my calendar, it's {month}",
    "It's {month} right now, {name}",
    "My system says we are in {month}."
]



# game: rps
bot_rps = [
    "Paper!",
    "Scissors!",
    "Rock!"
]

user_rps = [
    "rps",
    "game"
]

def rps():
    while True:
        print("=== ROCK, PAPER, SCISSORS ===")
        bot_game_rps = random.choice(bot_rps)
        user_game = str(input("Your move: ")).lower().strip()
        if any(char in unsup_rus for char in user_game):
            print("We are sorry, but this kind of symbols is not supported.")
            continue
        if user_game in close:
                    print(bot_name, "Successfully Closed.")
                    break
        user_game = user_game.translate(str.maketrans("", "", signs))
        if bot_game_rps == "Paper!" and user_game == "rock":
            print(bot_name, bot_game_rps, f"\n", random.choice(lost))
        elif bot_game_rps == "Paper!" and user_game == "scissors":
            print(bot_name, bot_game_rps, f"\n", random.choice(win))
        elif bot_game_rps == "Rock!" and user_game == "scissors":
            print(bot_name, bot_game_rps, f"\n", random.choice(lost))
        elif bot_game_rps == "Rock!" and user_game == "paper":
            print(bot_name, bot_game_rps, f"\n", random.choice(win))
        elif bot_game_rps == "Scissors!" and user_game == "paper":
            print(bot_name, bot_game_rps, f"\n", random.choice(lost))
        elif bot_game_rps == "Scissors!" and user_game == "rock":
            print(bot_name, bot_game_rps, f"\n", random.choice(win))
        elif bot_game_rps == "Paper!" and user_game == "paper":
            print(bot_name, bot_game_rps, f"\n", random.choice(tie))
        elif bot_game_rps == "Rock!" and user_game == "rock":
            print(bot_name, bot_game_rps, f"\n", random.choice(tie))
        elif bot_game_rps == "Scissors!" and user_game == "scissors":
            print(bot_name, bot_game_rps, f"\n", random.choice(tie))
        else:
            print("That is not a move. Use Rock Paper Scissors rules.")

# prohibited symbols
signs = "&@#$_()*':;!?~`|•√π÷×§∆}{=°^¥€¢£%©®™✓\",.<>/_‽¡¿¬±≠≤≥≈≡∞∫√∂∇∏∑‹›«»„+-"

# unsupported lang
unsup_rus = "йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"

forbidden = signs + unsup_rus
    
# register
user_db = load_user_data()
if user_db:
    name = user_db.get("username")
    user_age = user_db.get("age")
    bot_naming = user_db.get("botname")
    bot_aging = user_db.get("botage")
    user_region = user_db.get("city", "Unknown")
    print(f"Successfully logged in as {name}.")
    time.sleep(1.5)
else:
    print("=== REGISTRATION ===")
    # name choice
    while True:
        symbollen = 8
        max_symbollen = 24
        name = input("Please, enter your username: ")
        if any(char in forbidden for char in name):
            print("This kind of symbols is not supported.")
            continue
        elif is_fully_profane(name):
            print("The name must not contain curse words.")
            continue
        elif len(name) < symbollen:
            print("The username must contain at least 8 characters.")
            continue
        elif len(name) > max_symbollen:
            print("The username must not be longer than 24 characters.")
            continue
        else:
            user_db["username"] = name
            user_region = get_region()
            user_db["city"] = user_region
            break

# age choice
    while True:
        try:
            user_age = int(input("Please, enter your age: "))
            if user_age == 0:
                print("You must be at least 1 year old.")
                continue
            elif 1 <= user_age <= 99:
                user_db["age"] = user_age
                break
            else:
                print("The age numbers cannot be more than 2 digits.")
                continue
        except ValueError:
            print("There must be a number, not a letter.")
 
# bot name
    while True:
        try:
            bot_naming = str(input("Bot name: "))
            if any(char in forbidden for char in bot_naming):
                print("This kind of symbols is not supported.")
                continue
            elif is_fully_profane(bot_naming):
                print("The name must not contain curse words.")
                continue
            else:
                user_db["botname"] = bot_naming
                break
        except ValueEr
