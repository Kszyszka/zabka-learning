from django.urls import path
from . import views

urlpatterns = [
    path('<int:quiz_id>/', views.attend_quiz, name='attend_quiz'),
    path('results/', views.results, name='results'),
    path('guest/<int:quiz_id>/', views.attend_quiz_guest, name='attend_quiz_guest')
]