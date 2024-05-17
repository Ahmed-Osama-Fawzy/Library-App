from django.shortcuts import render
from Controlling.models import Book , Borrowing , Client , User
import datetime


def Home(request):
    context = {
        'Title':'Home',
    }
    return render(request,'client/Home.html',context)

def Borrow(request):
    LastId = (Borrowing.objects.last().Id)
    Id = int(LastId + 1)
    BookId = request.POST.get("Id")
    ClientId = 1
    BorrowDate = datetime.date.today()
    ReturnDate = BorrowDate+datetime.timedelta(days=5)
    if(Id and BookId and ClientId and BorrowDate and ReturnDate):
        data = Borrowing(Id=Id, BorrowDate=BorrowDate, ReturnDate=ReturnDate, ClientId=Client.objects.get(Id=ClientId), BookId=Book.objects.get(Id=BookId))
        data.save()
    context = {
        'Title':'BorrowBook',
        'Books':Book.objects.all(),
    }
    return render(request, 'client/BorrowBook.html',context)

def History(request):
    ClientId = 1
    data = Borrowing.objects.filter(ClientId=ClientId)
    returnedata = []
    for i in range(len(data)):
        num = data[i].Id
        edata = Borrowing.objects.get(Id=num).BookId
        Obj = {
            'Title':edata.Title,
            'Category':edata.Category,
            'Available':edata.Available,
            'BorrowDate':data[i].BorrowDate,
            'ReturnDate':data[i].ReturnDate
        }
        returnedata.append(Obj)
    print(returnedata)
    context = {
        'Title':'History',
        'data':returnedata,
        'rrr':[{'r':1},{'r':2}]
    }
    return render(request, 'client/History.html',context)

def Portifloio(request):
    context = {
        'Title':'Portifolio',
    }
    Username = request.POST.get("Username")
    Name = request.POST.get("Name")
    Email = request.POST.get("Email")
    Phone = request.POST.get("Phone")
    OldPassword = request.POST.get("OldPassword")
    NewPassword = request.POST.get("NewPassword")
    print("Bad")
    if(Username and Name and Email and Phone and OldPassword and NewPassword):
        print("Good")
        print(OldPassword,NewPassword)
        UN = User.objects.get(Password=OldPassword).Username
        print(UN)
        if(''.join(UN.split()) == ''.join(Username.split())):
            print("Very Good")
            data = Client(Id=Client.objects.get(Username=Username).Id , Username=Username , Name=Name, Email=Email , Phone=Phone)
            data.save()
            newdata = User(id=User.objects.get(Password=OldPassword).id , Username=Username , Rule=True, Password=NewPassword)
            newdata.save()
            context['Error'] = "Password Changed Successfuly"
        else:
            context['Error'] = "Sorry Can't Change Password, Test Again"
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