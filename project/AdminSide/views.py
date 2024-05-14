from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request , 'admin/Home.html')

def AddBook(request):
    return render(request , 'admin/AddBook.html')

def ModifyBook(request):
    return render(request , 'admin/ModifyBook.html')

def RemoveBook(request):
    return render(request , 'admin/RemoveBook.html')

def History(request):
    return render(request , 'admin/History.html')

def Portifolio(request):
    return render(request , 'admin/Portifolio.html')

def ShowBooks(request):
    return render(request , 'admin/ShowBooks.html')

def ShowBook(request):
    return render(request , 'admin/ShowBook.html')

def Logout(request):
    return render(request , 'Home.html')
