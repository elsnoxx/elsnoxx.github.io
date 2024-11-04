// proměnné
var index = 0;
var odpocinek = 5000;
var images = [
    '/img/javascript/slideshowImg/img1.jpeg', //0
    '/img/javascript/slideshowImg/img2.jpeg', //1
    '/img/javascript/slideshowImg/img3.jpeg', //2
    '/img/javascript/slideshowImg/img4.jpeg'  //3
];

function slideshow(){
    document.getElementById('obrazky').src = images[index];
    index++;
    if (index == images.length) {index = 0;}
    setTimeout("slideshow()",odpocinek);
}