document.addEventListener('DOMContentLoaded', function () {
    const addQuestionBtn = document.getElementById('add-question-btn');
    const questionsList = document.getElementById('questions-list');
    const submitQuizBtn = document.getElementById('submit-quiz-btn');
    const quizNameInput = document.getElementById('quiz-name');

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

        if (quizName && questions.length > 0) {
            // Tu dodaj kod do wysłania quizu do bazy danych
            console.log({
                quizName,
                questions
            });
            alert('Quiz został dodany do bazy danych.');
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
});
