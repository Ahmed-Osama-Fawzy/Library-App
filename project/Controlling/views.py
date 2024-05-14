from django.shortcuts import render

# Create your views here.

def MainHome(request):
    return render(request , 'MainHome.html')

def LogIn(request):
    return render(request , 'Login.html')

def SignUp(request):
    return render(request , 'Signup.html')