my_sequence = []
print("Zadávej číselné položky sekvence každou zvlášť.")
print("Zadávání čísel ukončíš jakýmkoliv nečíselným vstupem.")
user_input = True
while user_input == True:
    user_number_str = input("Zadej položku... ")
    if user_number_str.isnumeric() == True:
        user_number_int = int(user_number_str)
        my_sequence.append(user_number_int)
    else:
        user_input = False

print("Seznam před seřazením je vypsán níže:")
print(my_sequence)
exchange_happened = None
list_length = len(my_sequence)
counter = 0

while exchange_happened != False:
    exchange_happened = False
    for index in range(list_length - 1):
        if my_sequence[index] > my_sequence[index + 1]:
            temporary_number = my_sequence[index + 1]
            my_sequence[index + 1] = my_sequence[index]
            my_sequence[index] = temporary_number
            exchange_happened = True
    counter += 1

print(f"Počet provedených iterací: {counter}")
print("Třídění bylo ukončeno.")
print("Seřazený seznam je vypsán níže:")
print(my_sequence)
