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
    $(".meta").click(function(){
        $(".odpoved-meta").toggle();
        console.log("meta open");
    });
    $(".title").click(function(){
        $(".odpoved-title").toggle();
        console.log("title open");
    });
    $(".style").click(function(){
        $(".odpoved-style").toggle();
        console.log("style open");
    });
    $(".div").click(function(){
        $(".odpoved-div").toggle();
        console.log("div open");
    });
    $(".h").click(function(){
        $(".odpoved-h").toggle();
        console.log("h open");
    });
    $(".p").click(function(){
        $(".odpoved-p").toggle();
        console.log("p open");
    });
    $(".a").click(function(){
        $(".odpoved-a").toggle();
        console.log("a open");
    });
});