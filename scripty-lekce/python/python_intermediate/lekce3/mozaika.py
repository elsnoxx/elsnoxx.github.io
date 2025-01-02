# Import Colorama a další potřebné moduly
from colorama import init, Fore, Back, Style
import os
import random

# Inicializace Colorama
init()

# Funkce pro nastavení velikosti terminálu
def set_terminal_size(columns, rows):
    if os.name == 'nt':  # Windows
        os.system(f'mode con: cols={columns} lines={rows}')
    else:  # Linux, macOS
        os.system(f'printf "\\e[8;{rows};{columns}t"')

# Nastavení terminálu na 50 sloupců a 50 řádků
set_terminal_size(50, 50)

# Barvy pro výstup
my_colors = [
    Fore.BLUE, Fore.CYAN, Fore.GREEN, 
    Fore.MAGENTA, Fore.RED, Fore.WHITE, 
    Fore.YELLOW
]

# Vykreslení barevného výstupu
for outer_index in range(50):  # 20 řádků
    my_line = ""
    for inner_index in range(50):  # 20 sloupců
        my_line += random.choice(my_colors) + "█"  # Přidání barevného bloku
    print(my_line)  # Vytisknutí celého řádku najednou

# Reset barev po skončení
print(Style.RESET_ALL)

# Čekání na vstup pro ukončení programu
input("Stiskni Enter pro ukončení...")
