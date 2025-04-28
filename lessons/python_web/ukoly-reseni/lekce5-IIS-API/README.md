# Zadání úkolu: Práce s API - ISS

Vytvoř program v Pythonu, který bude komunikovat s veřejným API pro sledování Mezinárodní vesmírné stanice (ISS):

1. **Získej aktuální polohu ISS**  
   - Použij endpoint: `http://api.open-notify.org/iss-now.json`
   - Vypiš čas, zeměpisnou šířku a délku aktuální polohy ISS.

2. **Získej seznam lidí aktuálně ve vesmíru**  
   - Použij endpoint: `http://api.open-notify.org/astros.json`
   - Vypiš počet lidí ve vesmíru a jejich jména včetně toho, na které lodi se nacházejí.

3. **Uživatelské rozhraní**  
   - Nabídni uživateli jednoduché menu s volbami:
     1. Zobrazit aktuální polohu ISS
     2. Vypsat osoby ve vesmíru
     3. Konec

4. **Ošetři možné chyby**  
   - Ošetři situace, kdy API není dostupné nebo vrátí chybu.

*Bonus:*  
Zobraz čas v přehledném formátu (např. `DD.MM.YYYY HH:MM:SS`).

---
