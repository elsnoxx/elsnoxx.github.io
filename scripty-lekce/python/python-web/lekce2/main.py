import os
import prikazy
import menu
import utils
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    utils.clear_console()
    print(Fore.CYAN + "Hello, I am your AI assistant. How can I help you?\n")

    while True:
        menu.zobraz_menu()
        volba = input(Fore.YELLOW + "Zadejte číslo příkazu: ")
        utils.log_to_file(f"Uživatel zadal příkaz: {volba}")
        utils.clear_console()
        menu.zobraz_menu(volba)
        utils.zpracuj_prikaz(volba)
        
        
        

if __name__ == "__main__":
    main()
