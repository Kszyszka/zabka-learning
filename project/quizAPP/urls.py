from django.urls import path
from . import views

urlpatterns = [
    path("", views.quiz_list, name='quizlist'),
    path("quizlist/", views.quiz_list, name='quizlist'),
    path('create/', views.create_quiz, name='quizwizard'),
    path('quizzes/<int:quiz_id>/', views.question_list, name='questionlist'),
    path('testlist/',views.test_list,name='testlist'),
    path('guest/', views.test_list_guest, name='testlistguest'),
    path('stats/', views.stats, name="stats")
]