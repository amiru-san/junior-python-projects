import json

proh = ("@#$&-+()/*':;!?~`|•√π÷×§∆£¢€¥^°={}%©®™✓[]")

try:
    with open("data.json", "r", encoding="utf-8") as datafile:
        data = json.load(datafile)
except (FileNotFoundError, json.JSONDecodeError):
    print("Error: Data file does not exist or it was deleted. Creating a new one...")
    data = {
        "username": None,
        "password": None
    }

while True:
    user = input("Move: ").strip().lower()
    
    if user == "reg":
        username =  input("Create a username: ")
        password = input("Create a password: ")
    
        if any(char in proh for char in username) or any(proh in char for char in password):
            print("The input must contain letters, numbers and underscore only.")
            continue
        else:
            data["username"] = username
            data["password"] = password
            try:
                with open("data.json", "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4)
                    print("Register Successful")
            except FileNotFoundError:
                print("Error: Data file not found.")

# login
    elif user == "log":
        username2 =  input("Enter your username: ")
        password2 = input("Enter your password: ")
    
        if any(char in proh for char in username2) or any(char in proh for char in password2):
            print("The input must contain letters, numbers and underscore only.")
            continue
        elif username2 != data.get("username") or password2 != data.get("password"):
            print("Error: Incorrect username or password. Try again.")
            continue
        else:
            print("Logged in successfully.")
            log = True
         
        if log:
            print(f"Welcome, {username2}!")
            log = False
    else:
        print("Unknown command.")
