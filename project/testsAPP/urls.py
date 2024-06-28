from django.urls import path
from . import views

urlpatterns = [
    path("", views.attend, name='attend'),
    path('attend/<int:quiz_id>/', views.attend_quiz, name='attend_quiz')
]