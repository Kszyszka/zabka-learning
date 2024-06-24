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

document.getElementById('contact-link').addEventListener('click', function(event) {
    event.preventDefault();
    const contactSection = document.getElementById('contact');
    contactSection.classList.toggle('hidden');
});

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
