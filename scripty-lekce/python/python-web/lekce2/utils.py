import os
from datetime import datetime
from colorama import init

init(autoreset=True)

def clear_console():
    """
    Funkce pro vyčištění konzole. Používá příkaz specifický pro operační systém.
    Pokud je operační systém Windows (nt), použije příkaz 'cls', jinak 'clear' pro Linux/Mac.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def log_to_file(message):
    """
    Funkce pro zápis zprávy do souboru log.txt.
    Přidá časovou značku k zprávě a zapíše ji do souboru.
    Formátování data a času na formát 'YYYY-MM-DD HH:MM:SS'
    """
    try:
        now = datetime.now()
        formatted_now = now.strftime('%Y-%m-%d %H:%M:%S')
        with open('log.txt', 'a+') as f:
            f.write(f"{formatted_now}: {message}" + '\n')
            f.close()
    except FileNotFoundError:
        print('Soubor neexistuje.')
    
def read_from_file():
    """
    Funkce pro čtení obsahu souboru 'log.txt' a jeho výpis do konzole.
    """
    try:
        
        with open('log.txt', 'r') as f:
            content = f.read()
            f.close()

        for line in content.split('\n'):
            print(line)
    except FileNotFoundError:
        print('Soubor neexistuje.')