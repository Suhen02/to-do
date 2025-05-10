from django.shortcuts import render,get_object_or_404,redirect
from .models import Task,Register
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate

def todolist(request):
    
    if request.method=='POST':
        task=Task(
            values=request.POST.get('value'),
            priority=request.POST.get('priority'),
            user=request.user
        )
        if task.priority is None or task.priority=='':
            task.priority=200
        else:
            task.priority=int(task.priority)
            print(task.priority)
            
        task.save()
        task_count = Task.objects.filter(user=request.user).count()
        messages.success(request,task_count)
        return redirect('home') 
    else:
        return render(request,'index.html')
        
def deleteFun(request,pk):
    print("you enter delete ")
    item=get_object_or_404(Task,pk=pk)
    item.delete()
    
    return redirect('display')

def display(request):
    task=Task.objects.filter(user=request.user)
    task_count = Task.objects.filter(user=request.user).count()
    messages.success(request,task_count)
    return render(request,'task.html',{'data':task})

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password) 

        if user is not None:
            auth.login(request,user) 
            return redirect('home')
        else:
            messages.success(request,'Invalide credentials') 
            return redirect('login')
    return render(request,'login.html') 


def register(request):
    register=Register()
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password')
        password2=request.POST.get('confirm_password')

        if password1 == password2:
           if User.objects.filter(username=username).exists():
               messages.success(request,"This user name is already exist!!")
               return redirect('register')   
           elif User.objects.filter(email=email).exists():
               messages.success(request,"This is email is already exists!!")
           
           else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                return redirect('login')
        else: 
              print('hello suhen')
              messages.success(request,"both password is not matching")
              return redirect('register')
    return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('home')