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

function slideshow2() {
    const slides = document.querySelectorAll('.slide');
    let currentSlide = 0;
    const slideInterval = 5000; // Čas pro zobrazení jednoho slide (v ms)

    function nextSlide() {
        slides[currentSlide].classList.remove('showing');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('showing');
    }

    setInterval(nextSlide, slideInterval);
}


function slideshow3() {
    const slides = document.querySelectorAll('.slide3');
    let currentSlide = 0;
    const slideInterval = 5000; // Čas pro zobrazení jednoho slide (v ms)

    function nextSlide() {
        slides[currentSlide].classList.remove('showing3');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('showing3');
    }

    setInterval(nextSlide, slideInterval);
}


function slideshow4() {
    const slides = document.querySelectorAll('#slides4 .slide4');
    const slideDescription = document.getElementById('slide-description');
    let currentSlide = 0;
    const slideInterval = 2000; // Interval mezi slidy (v ms)

    function nextSlide() {
        // Skryje aktuální slide
        slides[currentSlide].classList.remove('showing4');
        
        // Změní index na další slide
        currentSlide = (currentSlide + 1) % slides.length;

        // Zobrazí další slide a aktualizuje popis
        slides[currentSlide].classList.add('showing4');
        slideDescription.textContent = `Aktuální slide: ${currentSlide + 1}`;
    }

    // Nastaví interval pro přepínání slidů
    setInterval(nextSlide, slideInterval);
}


function slideshow5() {
    const slides = document.querySelectorAll('#slides5 .slide5');
    const pauseButton = document.getElementById('pause');
    let currentSlide = 0;
    let playing = true;
    let slideInterval = setInterval(nextSlide, 2000); // Automatický přechod po 2 sekundách

    function nextSlide() {
        if (playing){
            slides[currentSlide].classList.remove('showing5');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('showing5');
        }
    }

    // Funkce pro pauzu slideru
    function pauseSlideshow() {
        pauseButton.innerHTML = 'Hraj';
        playing = false;
        clearInterval(slideInterval);
    }

    // Funkce pro spuštění slideru
    function playSlideshow() {
        pauseButton.innerHTML = 'Pauza';
        playing = true;
        slideInterval = setInterval(nextSlide, 2000);
    }

    // Přepínač pro tlačítko pauzy
    pauseButton.onclick = function() {
        if (playing) {
            console.log(playing);
            pauseSlideshow();
        } else {
            playSlideshow();
            console.log(playing);
        }
    };
}


function slideshow6() {
    const slides = document.querySelectorAll('#slides6 .slide6');
    const pauseButton = document.getElementById('pause6');
    const nextButton = document.getElementById('next6');
    const previousButton = document.getElementById('previous6');
    let currentSlide = 0;
    let playing = true;
    let slideInterval;

    function startSlideShow() {
        slideInterval = setInterval(nextSlide, 2000);
    }

    function stopSlideShow() {
        clearInterval(slideInterval);
    }

    function goToSlide(n) {
        slides[currentSlide].classList.remove('showing6');
        currentSlide = (n + slides.length) % slides.length;
        slides[currentSlide].classList.add('showing6');
    }

    function nextSlide() {
        goToSlide(currentSlide + 1);
    }

    function previousSlide() {
        goToSlide(currentSlide - 1);
    }

    function pauseSlideshow() {
        pauseButton.innerHTML = 'Hraj';
        playing = false;
        stopSlideShow();
    }

    function playSlideshow() {
        pauseButton.innerHTML = 'Pauza';
        playing = true;
        startSlideShow();
    }

    pauseButton.addEventListener('click', function() {
        if (playing) {
            pauseSlideshow();
        } else {
            playSlideshow();
        }
    });

    nextButton.addEventListener('click', function() {
        if (playing) pauseSlideshow(); // Zastaví se při manuálním posunu
        nextSlide();
    });

    previousButton.addEventListener('click', function() {
        if (playing) pauseSlideshow(); // Zastaví se při manuálním posunu
        previousSlide();
    });

    // Zahájení automatického přehrávání slideru
    startSlideShow();
}

