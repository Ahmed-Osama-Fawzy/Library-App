from django.shortcuts import render
from .models import Client , User , Book , Borrowing

# Create your views here.

def MainHome(request):
    Books = Book.objects.all()
    BooksNumber = Book.objects.count()
    ClientsNumber = Client.objects.count()
    BorrowingsNumber = Borrowing.objects.count()
    context = {
        'Title':'Home',
        'Books':Books,
        'BooksNumber':BooksNumber,
        'ClientsNumber':ClientsNumber,
        'BorrowingsNumber':BorrowingsNumber,
    }
    return render(request , 'MainHome.html',context)

def PLibrary(request):
    Books = Book.objects.all()
    
    context = {
        'Title':'Home',
        'Books': Books
    }
    return render(request , 'Library.html',context)


def LogIn(request):
    context = {
        'Title':'Log In',
        'Error':''
    }
    if request.method == 'POST':
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        Users = User.objects.all()
        if(Username and Password):
            for i in range(User.objects.count()):
                if Users[i].Username == Username and Users[i].Password == Password:
                    if(Users[i].Rule):
                        print("Client")
                        context['Username'] = Client.objects.get(Username=Username).Username
                        context['Phone'] = Client.objects.get(Username=Username).Phone
                        context['Email'] = Client.objects.get(Username=Username).Email
                        context['Name'] = Client.objects.get(Username=Username).Name
                        return render(request , 'Client/Home.html' ,context)
                    else:
                        print("Admin")
                        context['Username'] = User.objects.get(Username=Username).Username
                        return render(request , 'Admin/Home.html' ,context)
        context['Error'] = "Sorry Username or Password is Wrong, Try Again"
    return render(request , 'Login.html' ,context)

def SignUp(request):
    context = {
        'Title':'Sign Up',
        'Error':''
    }
    LastId = Client.objects.last().Id
    Id = int(LastId + 1)
    Username = request.POST.get("Username")
    Name = request.POST.get("Name")
    Phone = request.POST.get("Phone")
    Email = request.POST.get("Email")
    Password = request.POST.get("Password")
    Users = User.objects.all()
    print("Enter 0 Signup")
    if(Username and Password):
        print("Enter 1 Signup")
        for i in range(User.objects.count()):
            if Users[i].Username == Username and Users[i].Password == Password:
                context['Error'] = "Sorry This Username and Password Already Used" 
                return render(request , 'Signup.html' ,context)
            if Users[i].Username == Username and Users[i].Password != Password:
                context['Error'] = "Sorry This Username  Already Used" 
                return render(request , 'Signup.html' ,context)
            if Users[i].Username != Username and Users[i].Password == Password:
                context['Error'] = "Sorry This Password  Already Used" 
                return render(request , 'Signup.html' ,context)
    if(Username and Name and Phone and Email and Password):
        print("Enter 2 Signup")
        data = Client(Id=Id , Name=Name ,Email=Email , Phone=Phone , Username=Username)
        data.save()

        newdata = User(Username=Username , Rule=True , Password=Password)
        newdata.save()

        return render(request , 'Login.html' , context={'Title':'Log In'})
    
    return render(request , 'Signup.html' ,context)