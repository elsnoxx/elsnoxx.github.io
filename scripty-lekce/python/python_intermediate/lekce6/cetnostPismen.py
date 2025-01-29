import colorama
import os
os.system("cls")
colorama.init(autoreset="True")
print(colorama.Back.RED + colorama.Fore.WHITE + colorama.Style.BRIGHT +
    "Tento program zjišťuje četnost výskytu písmen v zadané větě.")
user_sentence = input("Zadejte anglickou větu pro zjišťování četnosti...").lower()
english_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
count_english_alphabet = len(english_alphabet)
character_occurence = []
sentence_length = len(user_sentence)
for index in range(count_english_alphabet):
    character_occurence.append(user_sentence.count(english_alphabet[index]))
print(character_occurence)
result = ""
for index in range(count_english_alphabet):
    result = result + english_alphabet[index] + " → " + str(character_occurence[index]) + " | "
    if (index + 1) % 4 == 0:
        result = result + "\n"
print(result)