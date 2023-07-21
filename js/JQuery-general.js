// Počkáme, až se načte celý dokument
$(document).ready(function() {
    // Nastavíme akci po kliknutí na obrázek
    $(".modal-img").on("click", function() {
      // Zobrazíme modální okno
      $("#modal").css("display", "block");
      // Nastavíme zdroj obrázku v modálním okně na ten, který byl kliknutý
      $("#img01").attr("src", $(this).attr("src"));
    });

    // Akce po kliknutí na zavírací ikonu
    $(".close").on("click", function() {
      // Skryjeme modální okno
      $("#modal").css("display", "none");
    });
  });