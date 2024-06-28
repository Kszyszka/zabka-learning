from django.urls import path
from . import views

urlpatterns = [
    path('<int:quiz_id>/', views.attend_quiz, name='attend_quiz')
]