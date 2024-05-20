from django.shortcuts import render

from Controlling.models import Book , Borrowing , Client , User
from datetime import datetime

# Create your views here.

def Home(request):
    context = {
        'Title':'Home',
    }
    return render(request , 'admin/Home.html',context)

def AddBook(request):
    LastId = (Book.objects.last().Id)
    Id = int(LastId + 1)
    Title = request.POST.get("Title")
    Author = request.POST.get("Author")
    Category = request.POST.get("Category")
    Description = request.POST.get("Description")
    Link = str("static/Covers")
    currentdate = str(datetime.date(datetime.now()).strftime("-%y-%m-%d/"))
    Image = str(request.POST.get("Cover"))
    Cover = str(Link+currentdate+Image)
    Av = request.POST.get("Available")
    Available = True if Av == "on" else False
    print(Av)
    print(Available)
    if(Id and Title and Author and Category and Description and Cover and (Available or True)):
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
        data.append(Title)
        data.append(Author)
        data.append(Category)
        data.append(Description)
        data.append(Cover)
        data.append(Available)
    else:
        data = ['','','','','','']
    
    context = {
        'Title':'ModifyBook',
        'Id':Id,
        'BTitle':data[0],
        'Author':data[1],
        'Category':data[2],
        'Description':data[3],
        'Cover':data[4],
        'Available':data[5],
    }

    TheId = request.POST.get("XId")
    NewTitle = request.POST.get("Title")
    NewAuthor = request.POST.get("Author")
    NewCategory = request.POST.get("Category")
    NewDesciption = request.POST.get("Description")
    NewCover = request.POST.get("Cover")
    NewAvilable = True if request.POST.get("Available") != "None" else False

    if(TheId and NewTitle and NewAuthor and NewCategory and NewCover and NewDesciption and (NewAvilable or True)):
        data = Book(Id=TheId,Title=NewTitle,Author=NewAuthor,Category=NewCategory,Description=NewDesciption,Available=NewAvilable,Cover=NewCover)
        data.save()
    else:
        pass

    return render(request , 'admin/ModifyBook.html',context)

def RemoveBook(request):
    if request.method == "POST":
        Id = request.POST.get("Id")
        if Book.objects.get(Id=Id):
            number = (Book.objects.last().Id)
            Book.objects.get(Id=Id).delete()
            for i in range(int(Id)+1,number):
                num = Book.objects.get(Id=i).Id
                Book.objects.get(Id=i).Id = int(num)-1
        else:
            print("Not Finded")
    
    context = {
        'Title':'RemoveBook',
    }
    return render(request , 'admin/RemoveBook.html',context)

def History(request):
    data = Borrowing.objects.all()
    returneddata = []
    for i in range(0,Borrowing.objects.count()):
        obj = {}
        CId = data[i].ClientId.Id
        BId = data[i].BookId.Id
        obj['BorrowId'] = data[i].Id
        obj['BorrowDate'] = data[i].BorrowDate
        obj['ReturnDate'] = data[i].ReturnDate
        obj['BookName'] = Book.objects.get(Id = BId).Title
        obj['BookCategory'] = Book.objects.get(Id = BId).Category
        obj['BookAvailable'] = Book.objects.get(Id = BId).Available
        obj['ClientName'] = Client.objects.get(Id = CId).Name
        returneddata.append(obj)
    print(returneddata)
    context = {
        'Title':'History',
        'data':returneddata,
    }
    return render(request , 'admin/History.html',context)

def Portifolio(request):
    context = {
        'Title':'Portifolio',
        'Error':''
    }
    if request.method == 'POST':
        Username = request.POST.get("Username")
        OldPassword = request.POST.get("OldPassword")
        NewPassword = request.POST.get("NewPassword")
        if(Username and OldPassword and NewPassword):
            UN = User.objects.get(Password=OldPassword).Username
            if(''.join(UN.split()) == ''.join(Username.split())):
                data = User(id=User.objects.get(Password=OldPassword).id , Username=Username , Rule=False, Password=NewPassword)
                data.save()
                context['Error'] = "Password Changed Successfuly"
            else:
                context['Error'] = "Sorry Can't Change Password, Test Again"
    
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