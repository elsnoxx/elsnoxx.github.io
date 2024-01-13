let slideIndex = 1;
;

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("demo");
  let captionText = document.getElementById("caption");
  if (n > slides.length) { slideIndex = 1 }
  if (n < 1) { slideIndex = slides.length }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
  captionText.innerHTML = dots[slideIndex - 1].alt;
}


function zvirata() {
  var zvirata = [
    "Lachtan", "Had", "Krtek", "Kráva", "Slon", "Ovce", "Krokodýl", "Žirafa", 
    "Tučňák", "Velryba", "Zebra", "Delfín", "Papoušek", "Velbloud", "Želva", 
    "Sova", "Medvěd", "Kůň", "Pes", "Kočka", "Lev", "Koza", "Nosorožec", 
    "Žralok", "Opice", "Ježek", "Slepice", "Chobotnice", "Prase", "Králík", 
    "Žába", "Klokan", "Tygr", "Dáša", "Fretka", "Jelen", "Jaguár", "Krokodýl", "Lasice", "Lynx", "Mloček",
    "Mravenečník", "Pantera", "Pavouk", "Pegas", "Rak", "Ryba", "Sob", "Tetřev", "Vlk", "Vosa", "Včela", "Zebrohlav", "Zebrožrout", "Zvíře"
];
  // zobrazeni textu
  var zvirataElement = document.querySelector(".zvirata");
  zvirataElement.style.display = "block";
  // Funkce pro generování náhodného názvu zvířete
  function generujNahodnyNazev() {
    var nahodnyIndex = Math.floor(Math.random() * zvirata.length);
    return zvirata[nahodnyIndex];
  }
  // funkce pro kontrolu zdali zvire uz neni vygenerovane
  function validace(zvirata_text, nahodny_nazev) {
    for (let i = 0; i < zvirata_text.length; i++) {
      if (zvirata_text[i] === nahodny_nazev) {
        return true;
      }
    }
    return false;
  }

  var zvirata_text = [];
  var nahodny_nazev;
  // generovani nahodnych zvirat
  for (let i = 0; i < 3; ) {
    nahodny_nazev = generujNahodnyNazev();
    if (!validace(zvirata_text, nahodny_nazev)) {
      zvirata_text.push(nahodny_nazev);
      i++;
    }
  }
  // pridani zvirat do stranky
  for (let i = 1; i <= 3; i++) {
    let text = document.getElementById(i);
    text.innerHTML = zvirata_text[i-1];
  }
}
showSlides(slideIndex)