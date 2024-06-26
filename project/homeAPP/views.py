from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'home/mainpage.html')

def main_join(request):
    return render(request, "home/join.html")

def aboutus(request):
    return render(request, "home/aboutus.html")

def terms(request):
    return render(request, "home/terms.html")

def contact(request):
    return render(request, "home/contact.html")