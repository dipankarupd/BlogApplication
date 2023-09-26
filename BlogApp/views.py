from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.utils import timezone

# Create your views here.

def index(req):
    blogs = Blog.objects.all()
    return render(req, 'index.html', {'blogs': blogs})


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
                return redirect('signup')

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


def logout(req):
    auth.logout(req)
    return redirect('/')


def unlog(req):
    return render(req, 'unlogerr.html')


@login_required
def createblog(req):
    if req.method == 'POST':

        title=req.POST['title']
        abstract = req.POST['abstract']
        description = req.POST['description']
        imageurl = req.POST['blogimage']

        print('title')
        blog = Blog(
            title=title,
            abstract=abstract,
            description=description,
            image_url = imageurl,
            author = req.user,
            timeOfPosting = timezone.now()
        )

        blog.save()
        return redirect('success_page')
    else:
        return render(req, 'blog.html')


def succeess(req):
    return render(req, 'success.html')


def detail(req, blogid):
    blog = get_object_or_404(Blog, id=blogid)
    return render(req, 'blogdetail.html', {'blog': blog})