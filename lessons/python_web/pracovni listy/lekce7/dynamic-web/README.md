# Ukázkový web – Dynamický obsah ve Flasku

Tento projekt slouží jako ukázka základních principů tvorby dynamického webu pomocí Pythonu a Flasku.

## Zadání úkolu

Vytvoř Flask aplikaci, která demonstruje:

- **Vkládání proměnných do šablon** – zobraz na stránce pozdrav s proměnným jménem.
- **Výpis seznamu a podmínky** – zobraz seznam uživatelů, případně informaci, že seznam je prázdný.
- **Generování tabulky z dat** – zobraz tabulku osob (jméno, věk) na základě seznamu slovníků.
- **Formulář a zpracování dat** – vytvoř stránku s formulářem, který po odeslání zobrazí odpověď uživatele.
- **Parametr v URL** – vytvoř stránku, která pozdraví uživatele podle jména zadaného v adrese.

Každá část je řešena samostatnou routou a šablonou.

## Jak spustit

1. Ujisti se, že máš nainstalovaný Python a Flask (`pip install flask`).
2. Spusť aplikaci příkazem:
   ```
   python app.py
   ```
3. Otevři webový prohlížeč a navštiv `http://localhost:5000`.

## Struktura projektu

- `app.py` – hlavní soubor s Flask aplikací a routami
- `templates/` – složka s HTML šablonami pro jednotlivé stránky

## Cíl

Cílem je pochopit, jak ve Flasku:

- předávat data do šablon,
- pracovat s cykly a podmínkami v Jinja2,
- zpracovávat formuláře,
- používat parametry v URL.

Projekt můžeš dále rozšiřovat podle vlastních nápadů.

