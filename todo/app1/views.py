from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.views import View

from .forms import *
from .models import *

class Asosiy(View):
    def get(self,request):
        if request.user.is_authenticated:
            m=Reja.objects.all()

            data = {"rejalar": Reja.objects.filter(foydalanuvchi=request.user),
                    "reja": m,
                    }
            return render(request, "todo.html", data)
        return redirect("login")
    def post(self,request,son):
        Reja.objects.create(
            sarlavha=request.POST.get("s"),
            vaqti=request.POST.get("v"),
            malumot=request.POST.get("m"),
            status=request.POST.get("st"),
            foydalanuvchi=request.user
        )
        return redirect("home")
class Reja_ochir(View):
    def get(self,request, son):
        Reja.objects.get(id=son).delete()
        return redirect("home")


class LoginView(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        log=request.POST.get("l")
        parol=request.POST.get("p")
        userlar=authenticate(request,username=log, password=parol)
        if userlar is None:
            return redirect("login")
        login(request,userlar)
        return redirect("home")
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("login")