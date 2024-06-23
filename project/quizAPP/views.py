from django.shortcuts import render, get_object_or_404
from .models import Quiz
from .forms import QuizForm

# Create your views here.

basepath = "..\\templates\\quiz\\"

def home(request):
    return render(request, f'{basepath}home.html')



def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.created_by = request.user
            quiz.save()
            #return redirect('quiz_list')  # Redirect to a view that lists quizzes
        else:
            form = QuizForm()

    return render(request, f'{basepath}quizwizard.html')


def add_question(request):
    pass



def quiz_list(request):
    quizzes = Quiz.objects.all()  # Replace Quiz with your actual Quiz model - to be added once 
    return render(request, f'{basepath}quizlist.html', {'quizzes': quizzes})  # Replace with your actual template for quiz list

def question_list(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quiz/questionlist.html', {'quiz': quiz})
