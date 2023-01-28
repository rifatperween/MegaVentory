from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from datetime import datetime, timedelta
import urllib
class AccountCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':('Username')})
        self.fields['password1'].widget.attrs.update({'placeholder':('Password')})        
        self.fields['password2'].widget.attrs.update({'placeholder':('Repeat password')})

# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    context = {}
    if request.method=='POST':
        username = request.POST.get("userID")
        password = request.POST.get("pass")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect')
    return render(request, 'login.html', context)
def signupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = AccountCreationForm()
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account was created for "+form.cleaned_data.get("username"))
            u = User.objects.filter(username=request.POST.get('username'))[0]
            return redirect('login')
    context = {'form':form}
    return render(request, 'signup.html', context)
    # return render(request, "signup.html")
@login_required(login_url='login')
def home(request):
    if request.method=="GET" and request.GET:
        toDel = request.GET.get('del')
        warehouseItem.objects.filter(id=toDel).update(hasShipped=True)
        # warehouseItem.save()
    context = {"products": warehouseItem.objects.filter(hasShipped=False)}
    return render(request, "home.html",context=context)
def logoutPage(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def addProduct(request):
    if request.method=="POST":
        product = request.POST.get("product")
        category = request.POST.get("category")
        warehouseItem.objects.create(name=product, category=category).save()
        print(product, category, 'created')
    return render(request, "addProduct.html")
@login_required(login_url='login')
def shipped(request):
    context = {"products": warehouseItem.objects.filter(hasShipped=True)}
    return render(request, "shipped.html",context)