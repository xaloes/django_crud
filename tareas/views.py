from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
# Create your views here.
def singup(request):    
    
    if request.method == 'GET':
        print('enviando formulario')
        return render(request,'singup.html',{   
            'form':UserCreationForm
        })
    else:
        print(request.POST)
        print('obteniendo datos')
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('tareas')
            except:
                return render(request,'singup.html',{   
                    'form':UserCreationForm,
                    'error':'El usuario ya existe'
                })
        else:            
            return render(request,'singup.html',{   
                'form':UserCreationForm,
                'error':'Las contraseñas no coinciden'
            })  


def home(request):
    return render(request,'home.html')

def registra(request):
    return HttpResponse('Usuario no registrado')

def tareas(request):
    return render(request,'tareas.html')

def salir(request):
    logout(request)
    return redirect('home')

def logarse(request):
    
    if request.method == 'GET':
        return render(request,'logarse.html', {
            'form': AuthenticationForm
        })
    else:
        print(request.POST)
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request,'logarse.html', {
                'form': AuthenticationForm,
                'error': 'Usuario no valido'
            })
        else:
            login(request,user)
            return redirect('tareas')