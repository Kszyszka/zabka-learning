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

function startNewQuiz() {
    alert('Rozpoczynanie nowego quizu...');
    
}
document.addEventListener('DOMContentLoaded', function() {
    // Funkcja do logowania użytkownika
    function loginUser(username) {
        localStorage.setItem('username', username);
        updateUserDisplay();
    }

    // Funkcja do wylogowania użytkownika
    document.getElementById('logout-link').addEventListener('click', function(event) {
        event.preventDefault();
        localStorage.removeItem('username');
        updateUserDisplay();
    });

    // Funkcja do aktualizacji wyświetlania nazwy użytkownika
    function updateUserDisplay() {
        const username = localStorage.getItem('username');
        const usernameDisplay = document.getElementById('username-display');
        if (username) {
            usernameDisplay.textContent = `Witaj, ${username}!`;
            document.getElementById('logout-link').style.display = 'inline';
        } else {
            usernameDisplay.textContent = 'Witaj, Użytkowniku!';
            document.getElementById('logout-link').style.display = 'none';
        }
    }

    // Wywołanie funkcji przy załadowaniu strony
    updateUserDisplay();
});

// Przykładowe logowanie użytkownika (do usunięcia lub modyfikacji w produkcji)
loginUser('JanKowalski'); // Zalogowanie przykładowego użytkownika
// Walidacja formularza kontaktowego
document.querySelector('#contact form').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    if (!name || !email || !message) {
        alert('Wszystkie pola są wymagane!');
        return;
    }

    alert('Formularz został wysłany!');
});
    // Funkcja do logowania użytkownika
    function loginUser(username) {
        localStorage.setItem('username', username);
        updateUserDisplay();
    }

    // Funkcja do wylogowania użytkownika
    document.getElementById('logout-link').addEventListener('click', function(event) {
        event.preventDefault();
        localStorage.removeItem('username');
        updateUserDisplay();
    });

   
