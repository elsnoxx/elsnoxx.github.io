$(document).ready(function() {
    $(".otazka").click(function(){
        var sec = $(this).attr("id");
        var text = ".odpoved-" + sec;
        $(text).toggle();
        console.log(text);
    });
    // Přidáme akci na kliknutí na panel-heading
    $(".panel-heading").click(function() {
        // Najdeme rodičovský panel
        var panel = $(this).parent();
        // Skryjeme všechny ostatní obsahy panelů
        $(".panel-content").not(panel.find(".panel-content")).slideUp();
        // Rozbalíme nebo sbalíme obsah tohoto panelu
        panel.find(".panel-content").slideToggle();
    });
});