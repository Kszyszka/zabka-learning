from django.shortcuts import render, HttpResponse

# Create your views here.

basepath = "..\\templates\\quiz\\"

def home(request):
    return render(request, f'{basepath}home.html')

def create_quiz(request):
    return render(request, f'{basepath}quizwizard.html')

def add_question(request):
    pass



def quiz_list(request):
    # to be implemented after adding working functionality for quizzes

    """
    quizzes = Quiz.objects.all()  # Replace Quiz with your actual Quiz model - to be added once 
    return render(request, 'quiz_list.html', {'quizzes': quizzes})  # Replace with your actual template for quiz list
    """ 
    return render(request,  f'{basepath}quizlist.html')
