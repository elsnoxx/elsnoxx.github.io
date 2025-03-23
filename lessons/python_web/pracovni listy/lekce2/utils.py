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
