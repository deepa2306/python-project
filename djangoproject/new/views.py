from django.shortcuts import render
from django.http import HttpResponse
from new.models import student

# Create your views here.
def Home(request):

    return render(request,"Home.html")

def Register(request):
    if request.method== "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        abc=student(name=name,email=email,phone=phone)
        abc.save()
    return render(request,"Register.html")
