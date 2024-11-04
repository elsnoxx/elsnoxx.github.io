
function countRabbits() {
    for (var i = 1; i <= 3; i++) {
        alert("Králík číslo " + i);
    }
}


function onButtonColorcChange() {
    var text = document.getElementById('text');
    var r = Math.floor(Math.random() * 250);
    var g = Math.floor(Math.random() * 250);
    var b = Math.floor(Math.random() * 250);
    text.style.color = 'rgb(' + r + ',' + g + ',' + b + ')';
}

function onButtonCalc() {
    var aEl = document.getElementById('a');
    var bEl = document.getElementById('b');
    var cEl = document.getElementById('c');
    var a = Number(aEl.value);
    var b = Number(bEl.value);
    var c = a + b;
    cEl.value = c;
}

function getMyInput(event) {
    event.preventDefault();
    let inputField = document.getElementById("myInput");
    alert(inputField.value);
  }