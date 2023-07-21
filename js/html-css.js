$(document).ready(function() {
    // Akce po kliknutí na zavírací ikonu
    $(".otazka").on("click", function() {
        // Skryjeme modální okno
        $(".odpoved").css("display", "block");
    });
    $(".designer").click(function(){
        $(".odpoved-designer").toggle();
        console.log("designer open");
    });
    $(".vyvojar").click(function(){
        $(".odpoved-vyvojar").toggle();
        console.log("vyvojar open");
    });
    $(".tester").click(function(){
        $(".odpoved-tester").toggle();
        console.log("tester open");
    });
    $(".seo").click(function(){
        $(".odpoved-seo").toggle();
        console.log("seo open");
    });
    $(".DOCTYPE").click(function(){
        $(".odpoved-DOCTYPE").toggle();
        console.log("DOCTYPE open");
    });
    $(".html").click(function(){
        $(".odpoved-html").toggle();
        console.log("html open");
    });
});