from django.shortcuts import render
from django.views import generic

def index(request):
    return render(request, 'ecommerce/index.html')

def products(request):
    return render(request, 'ecommerce/products.html')	
	
def about(request):
    return render(request, 'ecommerce/about.html')
	
def contact(request):
    return render(request, 'ecommerce/contact.html')