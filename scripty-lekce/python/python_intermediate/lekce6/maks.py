import random
first_number = None
second_number = None
third_number = None
fourth_number = None
fifth_number = None
total_sum = -1
total_product = -2
iteration = 0

def iterate():
    global first_number, second_number, third_number, fourth_number, fifth_number
    global total_product, total_sum
    first_number = random.randint(1,10)
    second_number = random.randint(1,10)
    third_number = random.randint(1,10)
    fourth_number = random.randint(1,10)
    fifth_number = random.randint(1,10)
    total_sum = first_number + second_number + third_number + \
    fourth_number + fifth_number
    total_product = first_number * second_number * third_number * \
    fourth_number * fifth_number
    
while total_sum != total_product:
    iterate()
    iteration += 1
    
print(f"Success. Iteration: {iteration}")
print(first_number, "|", second_number, "|", third_number, "|",
fourth_number, "|", fifth_number)