from django.shortcuts import render
from Controlling.models import Book
from datetime import datetime ,date

# Create your views here.

def Home(request):
    context = {
        'Title':'Home',
    }
    return render(request , 'admin/Home.html',context)

def AddBook(request):
    LastId = Book.objects.count()
    Id = int(LastId + 1)
    Title = request.POST.get("Title")
    Author = request.POST.get("Author")
    Category = request.POST.get("Category")
    Description = request.POST.get("Description")
    Link = 'static/Covers'
    currentdate = datetime.date(datetime.now()).strftime("-%y-%m-%d/")
    Image = request.POST.get("Cover")
    Cover = Link+currentdate+Image
    print(Cover)
    Available = True if request.POST.get("Available") != 'None' else False
    if(Id and Title and Author and Category and Description and Cover and Available):
        Insert = Book(Id=Id , Title=Title , Author=Author , Category=Category , Description=Description , Cover=Cover , Available=Available )
        Insert.save()
    context = {
        'Title':'AddBook',
    }
    return render(request , 'admin/AddBook.html',context)

def ModifyBook(request):
    Id = request.POST.get("Id")
    data = []
    if Id:
        Title = Book.objects.get(Id=Id).Title
        Author = Book.objects.get(Id=Id).Author
        Category = Book.objects.get(Id=Id).Category
        Description = Book.objects.get(Id=Id).Description
        Cover = Book.objects.get(Id=Id).Cover
        Available = Book.objects.get(Id=Id).Available
    else:
        pass
    context = {
        'Title':'ModifyBook',
        'BTitle':Title,
        'Author':Author,
        'Category':Category,
        'Description':Description,
        'Cover':Cover,
        'Available':Available,
    }
    return render(request , 'admin/ModifyBook.html',context)

def RemoveBook(request):
    context = {
        'Title':'RemoveBook',
    }
    return render(request , 'admin/RemoveBook.html',context)

def History(request):
    context = {
        'Title':'History',
    }
    return render(request , 'admin/History.html',context)

def Portifolio(request):
    context = {
        'Title':'Portifolio',
    }
    return render(request , 'admin/Portifolio.html',context)

def ShowBooks(request):
    context = {
        'Title':'Show Books',
        'Books' : Book.objects.all()
    }
    return render(request , 'admin/ShowBooks.html',context)

def ShowBook(request):
    context = {
        'Title':'ShowBook',
    }
    return render(request , 'admin/ShowBook.html',context)

def Logout(request):
    context = {
        'Title':'Logout',
    }
    return render(request , 'MainHome.html',context)
