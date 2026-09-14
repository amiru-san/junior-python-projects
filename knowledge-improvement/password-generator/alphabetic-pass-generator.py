from random import choice

lets = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

print("== ALPHABETIC PASSWORD GENERATOR ==")

while True:
    try:
        user = int(input("Password length: "))
        if user <= 0:
            print("Error: The password length cannot be negative!")
            continue
    except ValueError:
        print("Error: This is a alphabet-only generator!")
    print(f"\n" + "".join(choice(lets) for _ in range(user)) + f"\n")
