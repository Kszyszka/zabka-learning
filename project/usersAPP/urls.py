from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.login_view, name="signin"),
    path('signup', views.signup_user, name="signup"),
    path('logout', views.logout_user, name="logout")
]
