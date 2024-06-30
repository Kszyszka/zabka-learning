### Autorzy (Informatyka 2023/2024 Semestr 2. - Grupa Ćwiczeniowa nr. 2):
- #### Krzysztof Hager 52687 - Lider "Kszyszka@Github"
- #### Elian Godyń 52678 - "Eli3001@Github"
- #### Jakub Grzęda 52682 - "Keczuk@Github"
- #### Kacper Grzesik 52684 - "kgrzesik17@Github"
- #### Michał Fuławka 52675 - "MichalFulawka330@Github"
## [Link do repozytorium](https://github.com/Kszyszka/zabka-learning) - https://github.com/Kszyszka/zabka-learning
# Raport: Projekt Zaliczeniowy - Platforma e-learningowa z quizami i śledzeniem postępów. (***Qmaj Rzabe***)

## Wprowadzenie

Poniższy dokument zawiera dokumentację funkcjonalności każdego modułu (aplikacji) z projektu zabka-learning:
- HomeAPP
- UsersAPP
- QuizAPP
- TestsAPP

Wszystkie informacje w tym dokumencie odnoszą się do:
- project/static
- project/templates
- poject/(Aplikacje)

## HomeAPP
Jest to aplikacja obsługująca domyślny widok (stronę główną), oraz wszystkie wychodzące z niej połączenia:

1. Mainpage - Przenosi do panelu logowania/rejestracji (UsersAPP) lub do wykonania testu z poziomu Gościa (dostępne wszystkie Quizy na platformie).
![alt text](image-6.png)
2. Aboutus - Strona informacyjna, czym jest projekt qmaj rzabe.
![alt text](image-7.png)
3. Regulamin - Regulamin korzystania z aplikacji, wyświetlany jest plik static/terms.pdf w dedykowanym iframe.
![alt text](image-8.png)
4. Contact - Strona do kontaktu (można uzupełnić własne dane) oraz lokalizacji (OpenStreetMap).
![alt text](image-9.png)

## UsersAPP
UsersAPP to przedłużenie wbudowanego Django Auth, do logowania oraz rejestracji użytkowników. Konta mogą być usuwane oraz zarządzane z poziomu panelu administracyjengo (login: admin; hasło: admin).

1. Login - aplikacja do logowania użytkownika, redirect do QuizAPP
![alt text](image-10.png)
2. Signup - aplikacja do tworzenia użytkownika w bazie, automatycznie jest on logowany i przekierowywany do QuizAPP
![alt text](image-11.png)
3. Panel administracyjny - dostępny jest pod http://127.0.0.1:8000/admin; Wymaga bycia zalogowanym na konto administracyjne (domyślnie admin:admin), można dodać kolejnych użytkowników administracyjnych z jego poziomu, usuwać użytkowników, quizy, pytania, etc.
![alt text](image-12.png)

## QuizAPP
Jest to główna aplikacja, obsługująca backend, panel użytkownika oraz zarządzanie Quizami:

1. Struktura quizu i pytań w bazie danych (ORM):
![Quiz](image.png)
![Pytanie](image-1.png)
2. Podmoduły zawarte w QuizAPP:
    - Wyświetlanie listy quizów stworzonych obecnie zalogowanego użytkownika (z redirectem na detale odnośnie danego quizu – lista pytań i poprawne odpowiedzi).
![alt text](image-2.png)
    - Stwórz quiz
![alt text](image-3.png)
    - Rozpocznij nowy quiz (należący do ciebie), przekierowuje do TestsAPP
![alt text](image-4.png)
    - Statystyki rozwiązanych quizów (należących do ciebie)
![alt text](image-5.png)

## TestsAPP
Jest to aplikacja obsługująca rozwiązywanie testów przez użytkowników, zarówno zalogowanych jak i Gości (identyfikator użytkownika podaje się wtedy przy rozwiązywaniu testów).

1. Rozwiązywanie jako zalogowany użytkownik, z poziomu Panelu Użytkownika.
![alt text](image-13.png)
2. Rozwiązywanie jako Gość, z panelu Strony Głównej (HomeAPP).
![alt text](image-14.png)

Odpowiedzi zapisywane sa jako podejścia w bazie danych, do Test Attemps. Potem przekazywane są do QuizAPP, z poziomu którego widoczne są statystyki Quizów.