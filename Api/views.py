from django.shortcuts import render,redirect
#--->Importamos la Libreria de Permisos
from django.contrib.auth.decorators import login_required
#--->Importamos la Libreria de Logout
from django.contrib.auth import logout,login,authenticate
from .forms import *



# Create your views here.
def Home(request):
    return render (request,"Index.html")


def salir(request):
    logout(request)
    return redirect('Inicio')



def Registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method=='POST':
        query=CustomUserCreationForm(data=request.POST)
        if query.is_valid():
            query.save()
            user=authenticate(username=query.cleaned_data["username"],password=query.cleaned_data["password1"])
            login(request,user)
            
            return redirect('Inicio')
        data["form"]=query
    return render(request,"registration/registro.html",data)