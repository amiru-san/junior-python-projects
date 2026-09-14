from random import choice
import time

user = input("Password: ")

pack = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","1","2","3","4","5","6","7","8","9","0","@","#","$","_","&","-","+","(",")","/","*","'",":",";","!","?","~","`","|","•","√","π","÷","×","§","∆","£","¢","€","¥","^","°","=","{","}","%","©","®","™","✓","[", "]", " "]

found = []
attempts = 0
 
print(f"\n")
for target in user:
    while True:
        bot = choice(pack)
        attempts += 1
        time.sleep(0.001)
        
        print(f"Analyzing: {''.join(found)}{bot}", end="\r")
        
        if bot == target:
            found.append(str(bot))
            break
print(f"\nTarget Success: {"".join(found)}\nAttempts: {attempts}")
