from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def signupuser(request):
    htmlpath = "todo/signupuser.html"
    if request.method == 'GET':
        return render(request, htmlpath, {'form':UserCreationForm()})
    else:
        #Create new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')

            except IntegrityError:
                return render(request, htmlpath, {'form':UserCreationForm(), 'error':'Username already exisits, please choose another one'})


        else:
            # tell the user the passwords didn't match
            return render(request, htmlpath, {'form':UserCreationForm(), 'error':'Passwords need to match'})

def logoutuser(request):
    if request.method == 'POST': # has to be post request so that the borwser doesn't log you out 
        logout(request)
        return redirect('home')

def loginuser(request):
    htmlpath = "todo/loginuser.html"
    if request.method == 'GET':
        return render(request, htmlpath, {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])        
        if user is None:
            return render(request, htmlpath, {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            #(you were able to authinticate them, if the user was found and password matched then log them in
            login(request, user)
            return redirect('currenttodos')




def currenttodos(request):
    return render(request, 'todo/currenttodos.html')

def home(request):
    return render(request,'todo/home.html')



