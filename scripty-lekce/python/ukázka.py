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

