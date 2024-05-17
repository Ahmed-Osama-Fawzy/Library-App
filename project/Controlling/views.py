from django.shortcuts import render
from .models import Client , User

# Create your views here.

def MainHome(request):
    context = {
        'Title':'Home'
    }
    return render(request , 'MainHome.html',context)

def LogIn(request):
    context = {
        'Title':'Log In'
    }
    if request.method == 'POST':
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        Users = User.objects.all()
        if(Username and Password):
            for i in range(User.objects.count()):
                if Users[i].Username == Username and Users[i].Password == Password:
                    if(Users[i].Rule):
                        context['Username'] = Client.objects.get(Username=Username).Username
                        context['Phone'] = Client.objects.get(Username=Username).Phone
                        context['Email'] = Client.objects.get(Username=Username).Email
                        context['Name'] = Client.objects.get(Username=Username).Name
                        return render(request , 'Client/Home.html' ,context)
                    else:
                        context['Username'] = User.objects.get(Username=Username).Username
                        return render(request , 'Admin/Home.html' ,context)
    return render(request , 'Login.html' ,context)

def SignUp(request):
    LastId = Client.objects.last().Id
    Id = int(LastId + 1)
    Username = request.POST.get("Username")
    Name = request.POST.get("Name")
    Phone = request.POST.get("Phone")
    Email = request.POST.get("Email")
    Password = request.POST.get("Password")
    if(Username and Name and Phone and Email and Password):
        data = Client(Id=Id , Name=Name ,Email=Email , Phone=Phone , Username=Username)
        data.save()
        newdata = User(Username=Username , Rule=True , Password=Password)
        newdata.save()
        return render(request , 'Login.html' , context={'Title':'Log In'})
    context = {
        'Title':'Sign Up'
    }
    return render(request , 'Signup.html' ,context)