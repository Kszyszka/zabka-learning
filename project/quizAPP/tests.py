from django.test import TestCase
from models import Quiz, Question

# Create your tests here.
def QuizTest():
    tquiz = Quiz.objects.create(
        title="Python Programming Quiz",
        description="Test your knowledge of Python programming language."
    )

    ques1 = Question.objects.create(
        quiz=tquiz,
        question_text = "Ile to 9+10.",
        answer1 = "19",
        answer2 = "umm co do sigmy :D",
        answer3 = "21",
        answer4 = "jestes glupi nie jestem",
        correct_answer = 3  #poprawna odp to 21
    )
def test2():
    print('koniec testu')
