# Osobní web – Python Flask projekt

## Zadání

Vytvoř jednoduchý osobní web pomocí frameworku Flask. Web bude obsahovat několik stránek a bude využívat šablony a statické soubory.

### Požadavky:

- Použij Python a Flask.
- Web musí obsahovat minimálně tyto stránky:
  - **Domovská stránka** (`home.html`)
  - **O mně** (`about.html`)
  - **Kontakt** (`contact.html`)
- Každá stránka bude mít vlastní šablonu v adresáři `templates/`.
- Na stránkách použij obrázky z adresáře `static/img/`.
- Vytvoř jednoduchou navigaci mezi stránkami.
- Využij základní styly (můžeš použít Bootstrap nebo vlastní CSS).
- Spuštění aplikace bude zajištěno souborem `app.py`.

### Bonus:

- Přidej další stránku dle vlastního výběru (např. projekty, zájmy, galerie...).
- Přidej kontaktní formulář (odesílání nemusí být funkční).
- Použij dědičnost šablon (base template).

---

## Struktura projektu

```
lekce6-ukol/
├── app.py
├── static/
│   ├── img/
│   │   └── logos.jpg
│   └── css/
│       └── style.css
└── templates/
    ├── home.html
    ├── about.html
    ├── contact.html
```
---

## Jak spustit aplikaci

1. Nainstaluj Flask (např. `pip install flask`).
2. Spusť aplikaci příkazem:

   ```
   python app.py
   ```

3. Otevři webový prohlížeč a přejdi na adresu `http://localhost:5000`.

---

## Inspirace

- [Flask dokumentace](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)

---

> Projekt slouží k procvičení základů práce s Flaskem, šablonami a statickými soubory.