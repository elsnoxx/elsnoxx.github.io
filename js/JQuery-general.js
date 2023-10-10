// Počkáme, až se načte celý dokument
$(document).ready(function () {
  // Nastavíme akci po kliknutí na obrázek
  $(".myImg").on("click", function () {
    // Zobrazíme modální okno
    var altText = $(this).attr("alt");
    $(".modal").css("display", "block");
    // Nastavíme zdroj obrázku v modálním okně na ten, který byl kliknutý
    $("#img01").attr("src", $(this).attr("src"));
    $("#img01").attr("alt", altText);
    console.log(altText)
    $("#caption").text(altText);
  });

  // Akce po kliknutí na zavírací ikonu
  $(".close").on("click", function () {
    // Skryjeme modální okno
    $(".modal").css("display", "none");
  });

  // Akce po kliknutí na zavírací ikonu
  $(".modal").on("click", function () {
    // Skryjeme modální okno
    $(".modal").css("display", "none");
  });

});

function naplcas() {
  var datum = new Date();
  var hodiny = datum.getHours();
  var minuty = datum.getMinutes();
  var sekundy = datum.getSeconds().toString();

  if (minuty < 10) {
    minuty = "0" + minuty;
  }
  
  if (sekundy < 10) {
    sekundy = "0" +sekundy;
  }
  var aktualniCas = hodiny + ":" + minuty + ":" + sekundy;
  $("#cas").text(aktualniCas);
}


//intervalove spusteni funkce, musi pred tim byt i volani funkce
naplcas();
setInterval(naplcas, 1000);

function casovac() {
  var time10min = 1000 * 60 * 10;
  var countDownDate = new Date().getTime() + time10min;
  // Update the count down every 1 second
  var x = setInterval(function () {

    // Get today's date and time
    var now = new Date().getTime();

    // Find the distance between now and the count down date
    var distance = countDownDate - now;
    console.log(distance);

    // Time calculations for days, hours, minutes and seconds
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Output the result in an element with id="demo"
    document.getElementById("casovac").innerHTML = minutes + "m " + seconds + "s ";

    // If the count down is over, write some text 
    if (distance < 0) {
      clearInterval(x);
      document.getElementById("casovac").innerHTML = "EXPIRED";
    }
  }, 1000);

  casovac = function(){};
}

function passwd(){
  var password = prompt('Enter the password to download the file:');
  if(password.toLowerCase() == "teacher"){
    window.open("folder/history.zip")    
  }else{
    alert("incorrect password!! please try again");
  }
}

