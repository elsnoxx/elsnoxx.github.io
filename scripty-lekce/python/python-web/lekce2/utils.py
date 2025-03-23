import os
from colorama import init

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
