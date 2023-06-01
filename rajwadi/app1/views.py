from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError


# -----------------------------  home page  ------------------------------------------------

@login_required(login_url='/')
def home(request):
    return render(request, 'home.html')


# ---------------------------------login------------------------------------------

def login(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        print(username, pass1)
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            request.session['username'] = username
            request.session["name"] = "test"
            request.session["xyz"] = "test"
            auth_login(request, user)
            return redirect('home')
        else:
            return HttpResponse("username or password is incorrect!!!!!!!")
    return render(request, 'login.html')

# -------------------------------- register -----------------------------------------------


def register(request):
    if 'username' in request.session:
        return redirect(home)
    
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')

        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        pass_1 = request.POST.get('pass1')
        pass_2 = request.POST.get('pass2')
        if User.objects.filter(username=username).exists():
            error_message = "User already exists."
            return render(request, 'reg.html', {'error_message': error_message})

        if len(phone) != 10:
            return HttpResponse("number is not valid")

        if pass_1 != pass_2:
            return HttpResponse("your password not match")
        else:
            print(username, lastname, phone, email, pass_1, pass_2)
            my_user = User.objects.create_user(username, email, pass_1)
            my_user.first_name = firstname
            my_user.last_name = lastname
            print(my_user)
            my_user.save()

        return redirect('login')
    return render(request, 'reg.html')


# ------------------------forgot------------------------------------------------

def forgot(request):
    if 'username' in request.session:
        return redirect(home)
    if request.method == "POST":
        username = request.POST.get('username')
        code = 1234
        password = request.POST.get('newpassword')
        confirmpassword = request.POST.get('newpasswordconfirm')

        if password == confirmpassword:
            user = User.objects.get(username=username)
            new_password = password
            hashed_password = make_password(new_password)
            user.password = hashed_password
            user.save()
            return redirect('logins')
        else:
            return redirect('/forgotpassword')
    return render(request, 'forgot.html')


# ---------------------------logout----------------------------------------


@login_required(login_url='/')
def logoutpage(request):
    logout(request)
    return redirect('login')


# -------------------------user profile------------------------
@login_required
def user_profile(request):
    context = {}            
    all = User.objects.all()
    context["username"] = all
    return render(request, 'user_profile.html', context)


# -----------------update_profile=------------
@login_required(login_url='/')
def update_profile(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name =request.POST['last_name']
        
        user = User.objects.filter(username=request.user.username)
        if user.exists():
            user = user.first()
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        return redirect('user_profile')
    else:
        return render(request, 'profile_update.html')


