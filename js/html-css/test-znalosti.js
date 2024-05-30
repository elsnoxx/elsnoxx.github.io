// script.js
document.addEventListener('DOMContentLoaded', () => {
    const tasks = [
        'Vytvořte tučný text',
        'Vytvořte funkční odkaz na google.com',
        'Vytvořte tlačítko',
        'Vytvořte seznam s tečkami',
        'Vytvořte seznam s čísly',
        'Vytvořte největší nadpis',
        'Vytvořte nejmenší nadpis v modré barvě',
        'Vytvořte text kurzívou',
        'Přidejte obrázek o šířce 300px',
        'Vytvořte odkaz bez formátování, černý',
        'Rozdělte text na 2 řádky pomocí <br>',
        'Vytvořte červený text',
        'Vytvořte tabulku',
        'Vytvořte odstavec textu',
        'Použijte inline CSS pro změnu barvy textu na zelenou',
        'Použijte externí CSS soubor pro stylování textu na modro',
        'Vytvořte div s okrajem (border)',
        'Vytvořte div s vnitřním odsazením (padding)',
        'Vytvořte div s vnějším odsazením (margin)',
        'Vytvořte responsivní obrázek pomocí CSS',
        'Vytvořte tlačítko, které mění barvu při najetí myši',
        'Použijte flexbox pro zarovnání dvou divů vedle sebe',
        'Vytvořte jednoduchou navigační lištu',
        'Vytvořte formulář s textovým polem a tlačítkem odeslání'
    ];

    const examples = [
        '<b>Toto je tučný text</b>',
        '<a href="https://www.google.com">Toto je odkaz na Google</a>',
        '<button>Toto je tlačítko</button>',
        '<ul><li>Položka 1</li><li>Položka 2</li></ul>',
        '<ol><li>Položka 1</li><li>Položka 2</li></ol>',
        '<h1>Toto je největší nadpis</h1>',
        '<h6 style="color: blue;">Toto je nejmenší nadpis v modré barvě</h6>',
        '<i>Toto je text kurzívou</i>',
        '<img src="https://via.placeholder.com/300" alt="Ukázkový obrázek" width="300">',
        '<a href="#" style="text-decoration: none; color: black;">Toto je odkaz bez formátování</a>',
        'Řádek 1<br>Řádek 2',
        '<span style="color: red;">Toto je červený text</span>',
        '<table border="1"><tr><th>Hlavička</th></tr><tr><td>Bunka</td></tr></table>',
        '<p>Toto je odstavec textu.</p>',
        '<span style="color: green;">Toto je zelený text</span>',
        '<link rel="stylesheet" href="styles.css"><span class="blue-text">Toto je text s externím CSS</span>',
        '<div style="border: 1px solid black;">Toto je div s okrajem</div>',
        '<div style="padding: 20px; background-color: lightgray;">Toto je div s vnitřním odsazením</div>',
        '<div style="margin: 20px; background-color: lightgray;">Toto je div s vnějším odsazením</div>',
        '<img src="https://via.placeholder.com/300" alt="Ukázkový obrázek" style="max-width: 100%;">',
        '<button style="background-color: blue; color: white;">Toto je tlačítko</button><style>button:hover { background-color: green; }</style>',
        '<div style="display: flex;"><div style="flex: 1; background-color: lightblue;">Div 1</div><div style="flex: 1; background-color: lightcoral;">Div 2</div></div>',
        '<nav><ul style="list-style-type: none;"><li><a href="#">Home</a></li><li><a href="#">About</a></li><li><a href="#">Contact</a></li></ul></nav>',
        '<form><input type="text" placeholder="Váš text"><button type="submit">Odeslat</button></form>'
    ];

    let currentTaskIndex = 0;
    const taskElement = document.getElementById('task');
    const exampleElement = document.getElementById('example');
    const startButton = document.getElementById('start-task');

    startButton.addEventListener('click', () => {
        if (currentTaskIndex < tasks.length) {
            taskElement.innerText = tasks[currentTaskIndex];
            exampleElement.innerHTML = examples[currentTaskIndex];
            startButton.disabled = true;
            setTimeout(() => {
                alert('Čas vypršel!');
                startButton.disabled = false;
                currentTaskIndex++;
            }, 6); // 1 minuta na každý úkol
        } else {
            taskElement.innerText = 'Všechny úkoly jsou dokončeny!';
            exampleElement.innerHTML = '';
            startButton.disabled = true;
        }
    });
});
