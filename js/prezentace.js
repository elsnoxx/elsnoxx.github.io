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
    var slider = document.getElementById("background");
    var output = document.getElementById("back-code");

    output.innerHTML = slider.value; 
    
    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function () {
        output.innerHTML = this.value;
        console.log(this.value);
    }
}

function text(){
    var slider = document.getElementById("text");
    var output = document.getElementById("text-code");

    output.innerHTML = slider.value; 
    
    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function () {
        output.innerHTML = this.value;
        console.log(this.value);
    }
}

text();
barva();