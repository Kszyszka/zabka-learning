from django.urls import path
from . import views

urlpatterns = [
    path("", views.quiz_list, name='quizlist'),
    path('create/', views.create_quiz, name='quizwizard'),
    path('quizzes/<int:quiz_id>/', views.question_list, name='questionlist')
]