def while_cyklus():
    a = 0

    while a < 10:
        print("Number " + str(a))
        a = a + 1
    print("Konec cyklu")

def while_cyklus_break():
    a = 0
    while a < 10:
        print("Number " + str(a))
        if a == 5:
            break
        a = a + 1
    print("Konec cyklu")

def for_cyklus():
    a = 0
    for a in range(1,10):
        print("Number " + str(a))
        a = a + 1
    print("Konec cyklu")

def for_cyklus_break():
    a = 0
    for a in range(1,10):
        print("Number " + str(a))
        if a == 5:
            break
        a = a + 1
    print("Konec cyklu")



# # obyčejný while cyklus, který projede všech 10 čísel od 0 - 9
# print("obyčejný while cyklus, který projede všech 10 čísel od 0 - 9")
# while_cyklus()
# # while cyklus když a bude obsahovat číslo 5 cyklus ukončí
# print("while cyklus když a bude obsahovat číslo 5 cyklus ukončí")
# while_cyklus_break()
# # obyčejný for cyklus, který projede všech 10 čísel od 0 - 9
# print("obyčejný for cyklus, který projede všech 10 čísel od 0 - 9")
# for_cyklus()
# # for cyklus když a bude obsahovat číslo 5 cyklus ukončí
# print("for cyklus když a bude obsahovat číslo 5 cyklus ukončí")
# for_cyklus_break()


# ukázkový příklad, hádání čísla
# import random

# while True:
#     val = int(input("Zadej číslo: "))
#     num = random.randint(0, 10)
#     print("zadaná hodnota {}" )
#     if val == num:
#         break
#     else:
#         print("zkus to znova")
#         continue
    
# print(val,num)

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