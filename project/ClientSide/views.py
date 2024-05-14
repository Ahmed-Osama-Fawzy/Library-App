from django.shortcuts import render

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

def Logout(request):
    context = {
        'Title':'Home',
    }
    return render(request, 'MainHome.html',context)