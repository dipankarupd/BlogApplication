from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(req):
    return render(req, 'index.html')


def login(req):

    if(req.method == 'POST'):
        username = req.POST['username']
        password = req.POST['password']
    
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(req, user)
            return redirect('/')

        else:
            messages.info(req, 'Invalid credentials')
            return redirect('login')
    else:
        return render(req, 'signin.html')
        

def signup(req):
    
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(req, 'Email already exists')
                redirect('signup')

            elif User.objects.filter(username = username).exists():
                messages.info(req, 'Username already in use')
                return redirect('signup')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')

        
        else:
            messages.info(req,'Password do not match')
            return redirect('signup')
        
    else:
        return render(req, 'signup.html')