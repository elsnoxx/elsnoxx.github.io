// Počkáme, až se načte celý dokument
$(document).ready(function() {
    // Nastavíme akci po kliknutí na obrázek
    $(".myImg").on("click", function() {
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
    $(".close").on("click", function() {
      // Skryjeme modální okno
      $(".modal").css("display", "none");
    });
  });