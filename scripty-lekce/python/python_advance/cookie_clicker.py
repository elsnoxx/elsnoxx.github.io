import tkinter as tk
from math import ceil

# Inicializace základních proměnných
cookies = 0
cookies_per_click = 1
cookies_per_second = 0

# Počáteční ceny upgradů
upgrade_cost = 50
two_cookie_sec_cost = 150
one_cookie_sec_cost = 100
one_time_upgrade_cost = 200

# Funkce pro klikání na tlačítko
def click_cookie():
    global cookies
    cookies += cookies_per_click
    update_label()

# Funkce pro automatické generování cookies
def generate_cookies():
    global cookies
    cookies += cookies_per_second
    update_label()
    root.after(1000, generate_cookies)

# Funkce pro nákup vylepšení (zvyšuje cookies za klik)
def buy_upgrade():
    global cookies, cookies_per_click, upgrade_cost
    if cookies >= upgrade_cost:
        cookies -= upgrade_cost
        cookies_per_click += 1
        upgrade_cost = ceil(upgrade_cost * 1.1)
        update_label()

# Funkce pro nákup automatického generátoru cookies
def buy_auto_generator():
    global cookies, cookies_per_second, auto_generator_cost
    if cookies >= auto_generator_cost:
        cookies -= auto_generator_cost
        cookies_per_second += 1
        auto_generator_cost = ceil(auto_generator_cost * 1.1)
        update_label()

# Funkce pro nákup upgradu, který generuje 1 cookie za sekundu
def buy_one_cookie_per_sec():
    global cookies, cookies_per_second, one_cookie_sec_cost
    if cookies >= one_cookie_sec_cost:
        cookies -= one_cookie_sec_cost
        cookies_per_second += 1
        one_cookie_sec_cost = ceil(one_cookie_sec_cost * 1.1)
        update_label()

# Funkce pro jednorázový upgrade
def buy_one_time_upgrade():
    global cookies, cookies_per_click
    if cookies >= one_time_upgrade_cost:
        cookies -= one_time_upgrade_cost
        cookies_per_click += 5
        one_time_upgrade_button.pack_forget()
        update_label()

def buy_two_cookie_per_sec():
    global cookies, cookies_per_second, two_cookie_sec_cost
    if cookies >= two_cookie_sec_cost:
        cookies -= two_cookie_sec_cost
        cookies_per_second += 2
        two_cookie_sec_cost = ceil(two_cookie_sec_cost * 1.1)
        update_label()

# Aktualizace textu na obrazovce
def update_label():
    cookie_label.config(text=f"Cookies: {cookies}")
    cps_label.config(text=f"Cookies per second: {cookies_per_second}")
    cpc_label.config(text=f"Cookies per click: {cookies_per_click}")
    upgrade_button.config(text=f"Buy Upgrade ({upgrade_cost} cookies)")
    two_cookie_sec_button.config(text=f"Buy +2 Cps ({two_cookie_sec_cost} cookies)")
    one_cookie_sec_button.config(text=f"Buy +1 Cps ({one_cookie_sec_cost} cookies)")

# Vytvoření GUI
root = tk.Tk()
root.title("Cookie Clicker")
root.geometry("400x600")  # Nastavení velikosti okna
root.configure(bg="#f7e7ce")  # Nastavení barvy pozadí

# Horní rámec: Zobrazení cookies a statistik
top_frame = tk.Frame(root, bg="#fff2e6", pady=10)
top_frame.pack(fill="x")

cookie_label = tk.Label(top_frame, text=f"Cookies: {cookies}", font=("Helvetica", 18, "bold"), bg="#fff2e6", fg="#5a3e36")
cookie_label.pack()

cps_label = tk.Label(top_frame, text=f"Cookies per second: {cookies_per_second}", font=("Helvetica", 12), bg="#fff2e6", fg="#5a3e36")
cps_label.pack()

cpc_label = tk.Label(top_frame, text=f"Cookies per click: {cookies_per_click}", font=("Helvetica", 12), bg="#fff2e6", fg="#5a3e36")
cpc_label.pack()

# Prostřední rámec: Akční tlačítka
middle_frame = tk.Frame(root, bg="#f7e7ce", pady=20)
middle_frame.pack()

click_button = tk.Button(middle_frame, text="Click me!", command=click_cookie, width=20, height=2, font=("Helvetica", 14), bg="#ffd27f", fg="#5a3e36")
click_button.pack(pady=10)

# Spodní rámec: Upgrady
bottom_frame = tk.Frame(root, bg="#f7e7ce")
bottom_frame.pack()

upgrade_button = tk.Button(bottom_frame, text=f"Buy Upgrade ({upgrade_cost} cookies)", command=buy_upgrade, width=30, font=("Helvetica", 12), bg="#ffbf80", fg="#5a3e36")
upgrade_button.pack(pady=5)

one_cookie_sec_button = tk.Button(bottom_frame, text=f"Buy +1 Cps ({one_cookie_sec_cost} cookies)", command=buy_one_cookie_per_sec, width=30, font=("Helvetica", 12), bg="#ffbf80", fg="#5a3e36")
one_cookie_sec_button.pack(pady=5)

two_cookie_sec_button = tk.Button(bottom_frame, text=f"Buy +2 Cps ({one_cookie_sec_cost} cookies)", command=buy_two_cookie_per_sec, width=30, font=("Helvetica", 12), bg="#ffbf80", fg="#5a3e36")
two_cookie_sec_button.pack(pady=5)

one_time_upgrade_button = tk.Button(bottom_frame, text=f"Click Upgrade ({one_time_upgrade_cost} cookies)", command=buy_one_time_upgrade, width=30, font=("Helvetica", 12), bg="#ff8080", fg="#5a3e36")
one_time_upgrade_button.pack(pady=5)

# Spuštění generátoru cookies na pozadí
generate_cookies()

# Spuštění hlavní smyčky tkinter
root.mainloop()
