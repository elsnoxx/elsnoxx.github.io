$(document).ready(function() {
    $(".otazka").click(function(){
        var sec = $(this).attr("id");
        var text = ".odpoved-" + sec;
        $(text).toggle();
        console.log(text);
    });
});