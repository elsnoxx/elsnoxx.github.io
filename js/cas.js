function naplcas(){
    var datum = new Date();
    aktualniCas = datum.getHours() + "." + datum.getMinutes() + "." + datum.getSeconds();
    window.document.getElementsByID("cas").innerHTML = aktualniCas;
}
naplcas();
window.setInterval("naplcas()",1000);