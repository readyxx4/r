from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ProfileApp.models import *

def home(request):
    return render(request, 'home.html')
def login_view(request):
    return render(request, 'login.html')

def stock(request):
    return render(request, 'stock.html')

def productList(request):
    return render(request, 'product/productList.html')



def user_login(request):#ฟังก์ชันล็อกอิน
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Login success...")
        return redirect('home')
    else:
        messages.error(request, "Invalid username or password!!!")
        return redirect('user_login') # หรือ return redirect('home')
    
def user_logout(request):#ฟังก์ชันล็อกเอ้าท์
    logout(request)
    messages.info(request, "User logout...")
    return redirect('home')

def computerList(request):
    computers = Computer.objects.all()
    context = {'computers': computers}
    return render(request, 'product/computerList.html', context)

def computerOne(request, cid):
    computer = Computer.objects.get(cid=cid)
    context = {'computer':computer}
    return render(request,'product/computerOne.html',context)


def categoryList(request):
    categorys = Category.objects.all() 
    return render(request, 'categoryList.html', {'categorys': categorys})




