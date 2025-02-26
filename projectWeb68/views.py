from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def stock(request):
    return render(request, 'stock.html')
def productList(request):
    return render(request, 'product/productList.html')







