#úkol, naprogramování hry kámen nůžky papír
import random
# začátek hry
print("Hra bude mít 3 kola")
print("Ten kdo bude mít nejvíce bodů vyhraje")
print("Zadej velké písmeno pro výběr: ")
print("[R] - kámen")
print("[P] - papír")
print("[S] - nůžky")
# proměnné
bot_skore = 0
user_skore = 0
bot_choice = 0
user_choice = 0
varianty = ["R","P","S"]

print("------------------GAME STARTING------------------")
for i in range(3):
    print(("------------------ROUND {}------------------").format(i+1))
    user_choice = input("Tvoje volba: ")
    bot_choice = random.choice(varianty)
    print(("Bot má {} a ty {}").format(bot_choice,user_choice))
    if bot_choice == user_choice:
            print(("Remíza nikdo nezísakl bod v ROUND {}").format(i+1))
    elif bot_choice == "R":
        if user_choice == "S":
            bot_skore += 1
            print(("Bot vyhrál ROUND {}").format(i+1))
        else:
            user_skore += 1
            print(("Vyhrál jsi ROUND {}").format(i+1))
    elif bot_choice == "P":
        if user_choice == "R":
            bot_skore += 1
            print(("Bot vyhrál ROUND {}").format(i+1))
        else:
            user_skore += 1
            print(("Vyhrál jsi ROUND {}").format(i+1))
    elif bot_choice == "S":
        if user_choice == "P":
            bot_skore += 1
            print(("Bot vyhrál ROUND {}").format(i+1))
        else:
            user_skore += 1
            print(("Vyhrál jsi ROUND {}").format(i+1))
    

if bot_skore > user_skore:
    print("Bot vyhrál")
elif bot_skore < user_skore:
    print("Ty jsi vyhrál")
else:
    print("Remíza")