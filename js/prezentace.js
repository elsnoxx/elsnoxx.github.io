$(document).ready(function () {
    $(".otazka").click(function () {
        var sec = $(this).attr("id");
        var text = ".odpoved-" + sec;
        $(text).toggle();
        console.log(text);
    });
    // Přidáme akci na kliknutí na panel-heading
    $(".panel-heading").click(function () {
        // Najdeme rodičovský panel
        var panel = $(this).parent();
        // Skryjeme všechny ostatní obsahy panelů
        $(".panel-content").not(panel.find(".panel-content")).slideUp();
        // Rozbalíme nebo sbalíme obsah tohoto panelu
        panel.find(".panel-content").slideToggle();
    });
});


function barva() {
    var slider1 = document.getElementById("background");
    var output1 = document.getElementById("back-code");

    output1.innerHTML = slider1.value; 
    
    // Update the current slider value (each time you drag the slider handle)
    slider1.oninput = function () {
        output1.innerHTML = this.value;
        console.log(this.value);
    }

    var slider2 = document.getElementById("text");
    var output2 = document.getElementById("text-code");
    output2.innerHTML = slider2.value;
    slider2.oninput = function () {
        output2.innerHTML = this.value;
        console.log(this.value);
    }
}


barva();