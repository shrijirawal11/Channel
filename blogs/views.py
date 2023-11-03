from django.shortcuts import render, HttpResponse
from.models import post, writer
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    print('home3')
    return render(request,'home.html')


def aboutus(request):
    print('aboutus')
    return render(request,'about.html')

def testinomals(request):
    print('testinomals')
    return render(request,'testinomals.html')

def contact(request):
    print('contacts')
    return render(request,'contacts.html')

def blogs(request):
    print('blogs')
    feeds=post.objects.all()
    return render(request,'blogs.html',{'feeds':feeds})

def authors(request):
    print('blogs')
    writers=writer.objects.all()
    feeds=post.objects.all()
    return render(request,'authors.html',{'writers':writers, 'feeds': feeds}) 

def login(request):
    print('login')
    return render(request,'login.html')

def landing(request):
    print('page')
    writers=writer.objects.all()
    feeds=post.objects.all()
    return render(request,'landing.html',{'writers':writers, 'feeds': feeds}) 

def register(request):
    print('register') 
    if request.method =='POST':
        print(request.POST['username'], request.POST['email'])
        nm = request.POST['username']
        em = request.POST['email']
        pw = request.POST['password']
        if User.objects.filter(username = nm).exists():
            print("username Exist")
        elif User.objects.filter(email = em).exists():
            print("email Exist")
        else:
            user=User.objects.create_user(username=nm, email=em,password=pw)
            user.save()
            print('save')
        return render(request,'register.html')
    else:
        print('else')
        return render(request,'register.html')










