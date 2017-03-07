from django.contrib.auth import logout as django_logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic

def index(request):
    return render(request, 'ecommerce/index.html')

def products(request):
    return render(request, 'ecommerce/products.html')    
    
def about(request):
    return render(request, 'ecommerce/about.html')
    
def contact(request):
    return render(request, 'ecommerce/contact.html')

def user_login(request):
    return render(request, 'ecommerce/user/login.html')
	
def user_account(request):
    return render(request, 'ecommerce/user/account.html')
	
def user_products(request):
    return render(request, 'ecommerce/user/products.html')

def user_register(request):
    return render(request, 'ecommerce/user/register.html')
	
def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/ecommerce/') # Redirect after logout