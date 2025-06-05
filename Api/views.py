from django.shortcuts import render,redirect
#--->Importamos la Libreria de Permisos
from django.contrib.auth.decorators import login_required
#--->Importamos la Libreria de Logout
from django.contrib.auth import logout

# Create your views here.
def Home(request):
    return render (request,"Index.html")


def salir(request):
    logout(request)
    return redirect(to='inicio')



