from random import randint

print("== DIGITAL PASSWORD GENERATOR ==")

while True:
    try:
        user = int(input(f"\nPassword length: "))
        
        if user <= 0:
            print(f"Error: The password length cannot be negative!")
            continue
    except ValueError:
        print("Error: This is a digit-only generator!")
        continue
    print()
    for i in range(user):
        rand = randint(0, 9)
        print(rand, end="")
    print()
  #break – uncomment if you dont want an infinite loop dawg
