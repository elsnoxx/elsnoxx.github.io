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


function barvy() {

    var backgroundSlider = document.getElementById("background");
    var textSlider = document.getElementById("text");
    var backgroundOutput = document.getElementById("back-code");
    var textOutput = document.getElementById("text-code");
    var zobrazeni = document.getElementById("zobrazeni");

    // Update the background color and display the value
    backgroundSlider.oninput = function () {
        backgroundOutput.innerHTML = this.value;
        var backgroundColor = "rgb(" + textSlider.value + "," + textSlider.value+ "," + textSlider.value+")";
        var textColor = "rgb(" + textSlider.value + "," + textSlider.value+ "," + textSlider.value+")";

        zobrazeni.style.backgroundColor = backgroundColor;
        zobrazeni.style.color = textColor;
    };

    // Update the text color and display the value
    textSlider.oninput = function () {
        textOutput.innerHTML = this.value;
        var backgroundColor = "rgb(" + backgroundSlider.value + ", 0, 0)";
        var textColor = "rgb(" + textSlider.value + ", 0, 0)";

        zobrazeni.style.backgroundColor = backgroundColor;
        zobrazeni.style.color = textColor;
    };
}



barvy();


