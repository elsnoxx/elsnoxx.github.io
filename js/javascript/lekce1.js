// Funkce, která zobrazí alert
function zobrazAlert() {
    alert('Toto je zpráva z tlačítka!');
}

function toggleVisibility() {
    var text = document.getElementById('text');
    if (text.style.display === 'none') {
        text.style.display = 'block';
    } else {
        text.style.display = 'none';
    }
}

// funkce pro demonstrace prace s misi
var cursorDiv = document.getElementById('cursorPosition');
var output = document.getElementById('output');

// Sledování pohybu kurzoru
cursorDiv.addEventListener('mousemove', function (event) {
    output.textContent = 'X: ' + event.clientX + ', Y: ' + event.clientY;
});

// Kliknutí na prvek
cursorDiv.addEventListener('click', function () {
    alert('Klikli jste do této oblasti!');
});


function loadData() {
    var url = 'https://api.coingecko.com/api/v3/coins/bitcoin';

    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onload = function () {
        var outputBox = document.getElementById('output-AJAX');

        if (xhr.status === 200) {
            var data = JSON.parse(xhr.responseText);

            // Výpis informací o Bitcoinu
            var bitcoinInfo = `
                      <h5>${data.name} (${data.symbol.toUpperCase()})</h5>
                      <p>Cena v USD: $${data.market_data.current_price.usd}</p>
                      <p>Tržní kapitalizace: $${data.market_data.market_cap.usd}</p>
                      <p>24h Změna: ${data.market_data.price_change_percentage_24h}%</p>
                  `;
            outputBox.innerHTML = bitcoinInfo;
            outputBox.style.display = 'block'; // Zobrazení boxu po načtení dat
        } else if (xhr.status === 429) {
            outputBox.innerHTML = '<p>Limit API požadavků byl překročen. Zkuste to prosím později.</p>';
            outputBox.style.display = 'block'; // Zobrazení boxu i při chybě
        } else {
            outputBox.innerHTML = '<p>Došlo k chybě při získávání dat. Zkuste to prosím později.</p>';
            outputBox.style.display = 'block'; // Zobrazení boxu i při chybě
        }
    };
    xhr.onerror = function () {
        var outputBox = document.getElementById('output-AJAX');
        outputBox.innerHTML = '<p>Nepodařilo se připojit k API.</p>';
        outputBox.style.display = 'block'; // Zobrazení boxu při selhání
    };
    xhr.send();
}