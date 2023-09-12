function naplcas(){
    var datum = new Date();
    aktualniCas = datum.getHours() + ":" + datum.getMinutes() + ":" + datum.getSeconds();
    window.document.getElementById("cas").textContent = aktualniCas;
    console.log(aktualniCas);
}
naplcas();
window.setInterval(naplcas, 1000);
