import time

user = int(input("Введите число: "))

print(user)
time.sleep(1)
while True:
    user -= 1
    print(user)
    time.sleep(1)
    if user == 0:
        print("Время вышло!")
        break
