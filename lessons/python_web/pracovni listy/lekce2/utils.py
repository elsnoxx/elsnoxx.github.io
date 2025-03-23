import os
from colorama import init

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def zpracuj_prikaz(volba):
    """
    Funkce zpracovává uživatelskou volbu a volá odpovídající funkci podle čísla volby.

    Uživatel zadá číslo volby, které odpovídá konkrétní funkci. Funkce následně
    zavolá příslušnou funkci podle zadání. Pokud je volba neplatná, vypíše chybu.

    :param volba: Číslo volby, kterou uživatel zadal.
    """

def log_to_file(message):
    """
    Funkce pro zápis zprávy do souboru log.txt.
    Přidá časovou značku k zprávě a zapíše ji do souboru.
    Formátování data a času na formát 'YYYY-MM-DD HH:MM:SS'
    """

def read_from_file():
    """
    Funkce pro čtení obsahu souboru 'log.txt' a jeho výpis do konzole.
    """