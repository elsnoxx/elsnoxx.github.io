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
- K naleznutí rozbytých či nefunkčínch linků na web stránce. Se používá tento file [broken-links.py](scripty-sprava-webu/broken-links/broken-links.py). Ten po spuštění vygeneruje stránky a ta se následně zobrazí [zde](/bugs.html)

- Více informací v [README](scripty-sprava-webu/broken-links/README.md) této aplikace.

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
    - Vylepšní pdf pro domácí úkoly, z wordu nejlepe predelat vymyslet lepsi zpracovani
    - uprava novych obrazku na avif format
    - vytvorit scrypt pro konverzi uobrazku do avif formy, vytvorit k tomu readme
    - pridat tlacitka dropdown tak ze budou rozdelene podle tematickych okruhu, treba dropdown lekce -> okruhy -> jednotlive lekce
    - kouknout na https://github.com/xsuchy/programovani_pro_deti/tree/main
    - zkusit navrhnout seznam lekci pod card v boostrapu s fotky co se bude dit v lekci

    
    
- Art of presentation
    - zkusit udelat neco jako type war, abych omezil tolik externich odkazů
    
- Audacity
    - lekce 2 pridat ukazku fazovace, zrychleni tempa, orezat ticho
    - lekce 2 upravit pospi funkci podle https://manual.audacityteam.org/man/index_of_effects_generators_and_analyzers.html
    - lekce 3 pridat vytvareni tonu a tak
     
- Roblox
    - pridani obrazku k strance lekce 1, pridat datum pridani robloxu na windows 2006
    - pridani obrazku k strance lekce 2
    - pridani ukazku jak upravovat teren je to tlacitko Editor, a pote zalozka create se da vygenerovat teren, a v zalozce Edit je mozna editace terenu
    - pridani ukazky jak na kolaboraci mezi lidmi na jednom projektu
    - oprava scirptu na lekci 1
    - lekce 1 pridat ukazkovou hru
    - lekce 2 pridat ukazkovou hru
    - Lekce 3 - dodelat obsah
    - pridat stranku jak na kolaboraci, tkj spolu práci mezi vice lidmi na jednom projektu
    - lekce 3 vytvorit vkladani dalsich obrazku z roblox studia, musi to byt ve tvaru rbxassetid:// + ID toho obrázku
    - zmena pohledu osoby - starterplayer => Camera => cameramode == LockFirstPerson
    - Lekce 4 - samostatna prace
    - hodnoceni lekce   
    
- Python Beginer
    - lekce 6 obsah, zkontrolovat obsah
    - lekce 5, upravit ukol aby byl zajimavejsi + rozsirit to o pokracovani o seznamu

- Python Minecraft minetest
    - lekce 1 - dodelat rozpracovane chybi screeny
    - vytvorit scripty aby splnovali zadani samostatnych praci
    

- Construct 3
    - pridat ukazku chovani flash na space shooter
    
- Youtube
    - https://www.blackmagicdesign.com/products/davinciresolve

- Javascript
    - Nacrt co ukazovat ve vyuce https://www.jakpsatweb.cz/javascript/javascript-uvod.html
    
# Versions

## September 2024 - Update

- Python Minecraft minetest
    - word a pdf k projektu
    - projekt


- Javascript
    - Lekce 1 - pridan obsah lekce
    - Lekce 2 - pridan obsah lekce
    - Lekce 3 - pridan obsah lekce
    - Lekce 4 - pridan obsah lekce
    - Lekce 5 - pridan obsah lekce
    - IDE - popsani jakeho IDE budeme pouzivat v ramci Javascriptu


