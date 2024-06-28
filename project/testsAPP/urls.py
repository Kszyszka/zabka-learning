from django.urls import path
from . import views

urlpatterns = [
    path("", views.attend, name='attend')
]