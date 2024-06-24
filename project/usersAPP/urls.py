from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_home, name="userhome"),
    path('signin', views.login_view, name="signin"),
    path('signup', views.signup_user, name="signup"),
    path('joinquiz', views.join_quiz, name="joinquiz")
]
