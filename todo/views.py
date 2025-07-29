from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from todo.models import *
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.method == 'POST':
        fnm=request.POST.get('Username')
        email_id=request.POST.get('email')
        pwd=request.POST.get('password')
        print(fnm,email_id,pwd)
        my_user=User.objects.create_user(fnm,email_id,pwd)
        my_user.save()
        return redirect('/login')
    return render(request,'todo/signup.html')

def loginn(request):
    if request.method == 'POST':
        fnm=request.POST.get('Username')
        pwd=request.POST.get('password')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/todo')
        else:
            return redirect('/login')
    return render(request,'todo/login.html')

@login_required(login_url='/login/')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = Todo(title=title, user=request.user)  # Use Todo, not models.Todo
        obj.save()
        res = Todo.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo')
    res = Todo.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo/todo.html',{'res':res})

@login_required(login_url='/login/')
def edit_todo(request, srno):
    obj = Todo.objects.get(srno=srno, user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        obj.title = title
        obj.save()
        return redirect('/todo')
    return render(request, 'todo/edit_todo.html', {'todo': obj})

@login_required(login_url='/login/')
def delete_todo(request,srno):
    obj = Todo.objects.get(srno=srno, user=request.user)
    obj.delete()
    return redirect('/todo')

def signout(request):
    logout(request)
    return redirect('/login')