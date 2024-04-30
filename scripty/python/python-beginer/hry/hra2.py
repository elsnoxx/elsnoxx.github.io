import random

user_score = 0
user_choice = 0
door_count = 5
ghost_index = 0


print("Pravidla hry: ")
print(("Ukáže se vám {} dveří, za některými se schovává duch.").format(door_count))
print("Tvým úkolem je projít co jak nejvíce dveří aniž by jsi narazil a ducha.")
print("")
print("==========Hra začíná==========")

while True:
    print("==========Vyber dveře==========")

    for i in range(door_count):
        print(("[{}]").format(i+1))
    
    user_choice = int(input("Zadej číslo dveří: "))
    ghost_index = random.randint(1,door_count)
    print("==========Dveře se otevřeli==========")
    for i in range(1,door_count+1):
        if i != ghost_index:
            print("[   ]")
        else:
            print("[ G ]")
    # print(type(user_choice),type(ghost_index))
    
    if user_choice == ghost_index:
        print(("škoda prohrál jsi tvé skóre bylo {}").format(user_score))
        break
    elif user_choice != ghost_index:
        user_score += 1
        print("Tvé skóre je: ", user_score)
        print("==========Nové kolo==========")
    # break
