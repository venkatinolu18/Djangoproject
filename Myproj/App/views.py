from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Welcome to the Home Page!")
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html') 

def contact(request):
    return render(request, 'contact.html')

def pagenotfound(request, pagename):
    return HttpResponse(f"The page '{pagename}' was not found.", status=404)