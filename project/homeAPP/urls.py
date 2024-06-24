from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name="mainpage"),
    path('join', views.main_join, name="join"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('termsofuse', views.terms, name="terms"),
    path('contact', views.contact, name="contact"),
]
