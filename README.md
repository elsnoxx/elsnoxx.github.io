# Web pro lektorování ve Step It Academy

Tyto stránky byly vytvořené, pro vyučování v Step It academy. Je ze spousty učavy použitá pro vyučování dětí v oblasti IT. Veškeré lekce budou sepsané níže tak samo jako použité technologie při vývoji webu. 
Kažá lekce má určitý počet lekcí a na každé lekce si každý studen vytvoří **Závěrečnou prácí** z daného témata. A poté každý student odprezentuje před svími rodiči.


## Technologie
- HTML & CSS, Boostrap
- Javascript, JQuery
- Google Analytics
- Construct-3
- AVIF pro obrázky

## Broken links checker
- K naleznutí rozbytých či nefunkčínch linků na web stránce. Se používá tento file [broken-links.py](scripty/python/broken-links/broken-links.py). Ten po spuštění vygeneruje stránky a ta se následně zobrazí [zde](/bugs.html)

- Více informací v [README](scripty/python/broken-links/README.md) této aplikace.

## AVIF konverze

Ke konverzi obrazků na .avif stačí [GIMP](https://www.gimp.org/). A při použití funkce export jde obraze vyexportovat na .avif fomát. Formát podporují všecny nejpoužívanější vyhledávače. Enge pouze od verze 121.xx.


## Google Analytics

Google analytic využíváme ke sledování dění na webových stránkách. [WEBove rozhrani](https://analytics.google.com/analytics/web/#/p411707114/reports/reportinghub?params=_u..nav%3Dmaui&collectionId=business-objectives)

- Pokud je potřeba vytvořit novou stránku stačí přidat do head tagu v html dokumentu.

 ``` html
 <script async src="https://www.googletagmanager.com/gtag/js?id=G-4XPWG9HLN2"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    gtag('js', new Date());

    gtag('config', 'G-4XPWG9HLN2');
  </script>
 ```

## Google Analytics

Tato technologie je stále v rozmýšlení. Při poslední pokusu o zprovoznění tedy dne 16/10/2023. Bylo schválení zamítnuto z důvodu nedostatečného kontentu.

## Google ligthouse

Tato vyhytávka se skvěle hodní na nalezení chybějících věcí na webové stránce. Při vytvoření nové webové stránky, stránka projde kontrolou. Průměrný výsledek jde videt níže.
<figure style="text-align: center;">
<img src="img/vysledek-lighthouse.png" alt="vysledek ohodnoceni webu">
<figcaption markdown="2">
</figcaption>
</figure>

## ToDo List
- General
    - Vylepšení rozvržení hlavních stránek lekci, vytvoření sekcí 
     ``` html
        <section>
            text goes here
        </section>
    ```
    
- Roblox
    - pridani obrazku k strance env
    - pridani obrazku k strnace lua
    - pridani obrazku k strance lekce 1
    - pridani obrazku k strance lekce 2
    - oprava scirptu na lekci 1
    - lekce 1 pridat ukazkovou hru
    - lekce 2 pridat ukazkovou hru
    - Lekce 3 - dodelat obsah
    - [ ] Lekce 4 - obsah
    - [ ] Lekce 4 - samostatna prace
    - [ ] Projekt word a pdf
    - pridani ukazky jak zmenit barvu pomoci scriptu, nize ukazka nastavi objekt na cervenou barvu
        ``` lua
        local platform = script.Parent
        platform.BrickColor = BrickColor.Red()
        ```
    
- Construct
    - [ ] pridat ukazku chovani flash na space shooter
 

# Versions

## 20240205 - Update
- Roblox
    - Vytvoření lekce 2
    - Vytvoření Lekce 3
    - Vytvoření Lekce 4
- Art of presentation
    - Oprava správného zobrazení tabulky na strance projekt.html
- Youtube
    - pridat popisky obsahu k uvodu cele lekce

## 20240126 - Update
- Roblox
    - Vytvoření env, kde se popisují základní vlastnosti v Roblox studiu
    - Vytvoreni stranky o jazyku LUA a jeho základní syntaxe
    - Vytvoření obsahu lekce 1, spolu i vytvořené výsledné skripty

## 20240122 - Update
- General
    - Úprava dokumentace k webu
    - Vytvoření stánky kde budou zobrazeny updaty webovek
    - Upravit nove pridane fotky na avif format
- Audacity
    - pridani ukazky metadat na prvni lekci
    - pridani k ukolum a samostatných pracích pozadavek na metadata, tak jako v projektu zvukova kolaz
- Youtube
    - Lekce 3 - obsah
    - Lekce 4 - obsah
- Python Beginer
    - změmit Pycharm na vsc   
- TinkerCad
    - Oprava formatovani obrazku
- Roblox
    - Projekt web stranka

## 20240119 - Update
- TinkerCad
    - Přidat popisky k obrázkům
- Arf of presentation
    - Oprava textu na poslední lekci
    - optimalni velikost nadpisu a text
- Audacity
    - upravit nadpisi lekci na Lekce 1 - co se bude dit
    - oprava lekce 1 a klikaci odpovedi
- GENERAL
    - opravit broken links
    - vytvoření ikony webu
    - Přidat na stranky 
        ```html
        <meta name="description" content="popis stranky">
        ```

## 1/18/2024 - Update
- Google analytic 
    - [x] zprovozneni google analytic, pro monitorovani traficku na webovce
- Stranka pro prezentaci 
    - [x] vytvorit odkaz na hlavní stránce
    - [x] vytvorit pdf a word verzi pro ukoly
    - [x] upravit rozlozeni textu
- Youtube
    - [x] lekce 1
    - [x] lekce 2
    - [x] Lekce 5
    - [x] Projekt
    - [x] Upravit ukoly přidat informace
    - [x] Upravit poradí samostatných prací
    - [x] vytovření úkolů
- Construct
    - [x] lekce 3
    - [x] lekce 4
    - [x] lekce 5
    - [x] Lekce 6
    - [x] Lekce 7
    - [x] odevzdani du
    - [x] popsani prostredi constructu
    - [x] ukaždé prace přidat i ukázkovou práci
    - [x] přidání obrázky animace do lekce 2
    - [x] vytvoření stránky pro nejlepší projekty
    - [x] pridani k hram otevirani v dalsim okne
- TinkerCad
    - [x] přidání času a tlačítka na přeskakování mezi lekci
    - [x] uprava uvodni stranky
    - [x] vytvoření přehledu kde bude název skupiny a odkaz na přihlášení 
    - [x] Vytvoření zadání pro projekt, pdf a word, odkaz na stazeni zdani na stranku projektu
    - [x] projekt ZOO, random 3 zvirata z tohoto seznamu, ty zpracuji a vytvori zoo
    - [x] upravit nadpis lekce 1, 2, 3, 4, 5
    - [x] pridat odkaz na stranku tinkercadu na kazdou lekci a stranku projektuja-th-o-10-23
    - [x] vytvoreni skupiny na tinkercad + pristupove udaje ja-th-o-10-23
    - [x] pridani jedne bonusove prace
    - [x] uprava lekce 1
    - [x] smazat hodnocení ukolů
- Arf of presentation
    - [x] Lekce 1 - obsah
    - [x] Lekce 1 - kontrast barvy textu na strance
    - [x] Lekce 1 - samostatna prace
    - [x] Lekce 2 - samostatna prace
    - [x] Hodnoceni projektu
    - [x] Lekce 2 - obsah
    - [x] Lekce 3 - obsah
    - [x] Lekce 3 - samostatna prace
    - [x] Lekce 4 - obsah
    - [x] Lekce 4 - samostatna prace
    - [x] Projekt, word verze i pdf
    - [x] Rozdělení obrázku do složek podle lekce
    - [x] Vytvoření tabulky hodnoceni na strance projektu 
- Youtube
    - [x] novy projekt + prezentace
    - [x] oprava odkazu na strance projektu
    - [x] pridani stazeni coveru
- Python
    - [x] Prejmenovani na python_beginer
- General
    - [x] Opravit linky po zmene nazvu html stranek v tinkercad lekci
    - [x] Vytvořit footer
    - [x] Upravit obrázky, chyba je ve velikosti obrázků a rozměrech, kouknout na formaty AVIF nebo WebP
    - [x] Oprava obrazku kvuli ruznych prohlizecu Edge to nebere
    - [x] Sjednoceni navbaru, tak aby nikde nechybeli lekce
    - [x] Klikaci odkaz na nadpisi lekce, hodnoceni, projek a prezentace v prehledu lekce
        - [x] Arf of presentation
        - [x] Audacity
        - [x] Youtube
        - [x] TinkerCad
        - [x] Construct
        - [x] Roblox
        - [x] HTML and CSS
        - [x] Wordpress
        - [x] Javascript
        - [x] Python Beginer