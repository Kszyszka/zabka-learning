document.addEventListener('DOMContentLoaded', function () {
    const addQuestionBtn = document.getElementById('add-question-btn');
    const submitQuizBtn = document.getElementById('submit-quiz-btn');
    const quizNameInput = document.getElementById('quiz-name');
    const quizDescriptionInput = document.getElementById('quiz-description')
    const questionsList = document.getElementById('questions-list');

    let questions = [];

    addQuestionBtn.addEventListener('click', function () {
        const question = document.getElementById('question').value;
        const answer1 = document.getElementById('answer1').value;
        const answer2 = document.getElementById('answer2').value;
        const answer3 = document.getElementById('answer3').value;
        const answer4 = document.getElementById('answer4').value;
        const correctAnswer = document.getElementById('correct-answer').value;

        if (question && answer1 && answer2 && answer3 && answer4 && correctAnswer) {
            const newQuestion = {
                question,
                answers: [answer1, answer2, answer3, answer4],
                correctAnswer
            };

            questions.push(newQuestion);
            displayQuestions();

            document.getElementById('create-quiz-form').reset();
        } else {
            alert('Proszę wypełnić wszystkie pola.');
        }
    });

    submitQuizBtn.addEventListener('click', function () {
        const quizName = quizNameInput.value;
        let quizDescription = quizDescriptionInput.value;

        if (quizDescription.length == 0) {
            quizDescription = 'Nie dodano opisu.';
        }

        if (quizName && questions.length > 0) {
            const formData = {
                quizName,
                questions,  // This line was modified to match the expected structure
                quizDescription
            };
    
            fetch('/quiz/create/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')  // Ensure CSRF token is sent
                },
                body: JSON.stringify(formData)
            })
            .then(response => {
                if (response.ok) {
                    alert('Quiz został dodany do bazy danych.');
                    window.location.href = '../quizlist';  //hardcoduje to mam dosyć
                    return response.json();
                } else {
                    throw new Error('Failed to add quiz.');
                }
            })
            .catch(error => {
                console.error('Error:',error);
            });
        } else {
            alert('Proszę podać nazwę quizu i dodać przynajmniej jedno pytanie.');
        }
    });

    function displayQuestions() {
        questionsList.innerHTML = '';
        questions.forEach((q, index) => {
            const li = document.createElement('li');
            li.textContent = `${index + 1}. ${q.question} (Poprawna odpowiedź: ${q.correctAnswer})`;
            questionsList.appendChild(li);
        });
    }

    // Function to retrieve CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
