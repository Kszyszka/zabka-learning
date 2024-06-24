window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    header.classList.toggle('hide', window.scrollY > 0);

    const footer = document.getElementById('footer');
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        footer.classList.add('show');
    } else {
        footer.classList.remove('show');
    }
});

document.getElementById('home-link').addEventListener('click', function(event) {
    event.preventDefault();
    hideAllSections();
    document.getElementById('home').classList.remove('hidden');
});

document.getElementById('about-link').addEventListener('click', function(event) {
    event.preventDefault();
    hideAllSections();
    document.getElementById('about').classList.remove('hidden');
});

document.getElementById('contact-link').addEventListener('click', function(event) {
    event.preventDefault();
    hideAllSections();
    document.getElementById('contact').classList.remove('hidden');
});

document.getElementById('quizy-link').addEventListener('click', function(event) {
    event.preventDefault();
    hideAllSections();
    document.getElementById('quizy').classList.remove('hidden');
});

document.getElementById('settings-link').addEventListener('click', function(event) {
    event.preventDefault();
    hideAllSections();
    document.getElementById('settings').classList.remove('hidden');
});

function hideAllSections() {
    const sections = document.querySelectorAll('main section');
    sections.forEach(section => section.classList.add('hidden'));
}

let slideIndex = 0;
showSlides();

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.display = "block";
    setTimeout(showSlides, 3000); // ustawic mozna inny czas 
}

function continueQuiz() {
    alert('Kontynuowanie quizu...');
    
}

function startNewQuiz() {
    alert('Rozpoczynanie nowego quizu...');
    
}
