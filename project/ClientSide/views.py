from django.shortcuts import render
from Controlling.models import Book


def Home(request):
    context = {
        'Title':'Home',
    }
    return render(request,'client/Home.html',context)

def Borrow(request):
    context = {
        'Title':'BorrowBook',
    }
    return render(request, 'client/BorrowBook.html',context)

def History(request):
    context = {
        'Title':'History',
    }
    return render(request, 'client/History.html',context)

def Portifloio(request):
    context = {
        'Title':'Portifolio',
    }
    return render(request, 'client/Portifolio.html',context)

def Library(request):
    context = {
        'Title':'Library',
        'Books':Book.objects.all(),
    }
    return render(request, 'client/Library.html',context)

def CShowBook(request):
    context = {
        'Title':'ShowBook',
    }
    return render(request, 'client/ShowBook.html',context)

def Logout(request):
    context = {
        'Title':'Home',
    }
    return render(request, 'MainHome.html',context)