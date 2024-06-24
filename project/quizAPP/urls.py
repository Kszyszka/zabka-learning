from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name='home'),
    path('create/', views.create_quiz, name='quizwizard'), 
    path('quizlist/', views.quiz_list, name='quizlist'),
    path('quizzes/<int:quiz_id>/', views.question_list, name='questionlist'),
    path('add_question/', views.add_question, name='add_question')
]

