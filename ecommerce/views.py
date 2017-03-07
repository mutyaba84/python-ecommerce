from django.contrib.auth import authenticate, login, logout as django_logout # Use alias like "django_logout" so that django doesnt get confused on which function to use.
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
	if len(request.body) > 0: 
		# Process the request if posted data are available
		username = request.POST['username']
		password = request.POST['password']
		# Check username and password combination if correct
		user = authenticate(username=username, password=password)
		if user is not None:
			# Save session as cookie to login the user
			login(request, user)
			# Success, now let's login the user. 
			return render(request, 'ecommerce/user/account.html')
		else:
			# Incorrect credentials, let's throw an error to the screen.
			return render(request, 'ecommerce/user/login.html', {'error_message': 'Incorrect username and / or password.'})
	else:
		# No post data availabe, let's just show the page to the user.
		return render(request, 'ecommerce/user/login.html')
		
def user_account(request):
    return render(request, 'ecommerce/user/account.html')
	
def user_products(request):
    return render(request, 'ecommerce/user/products.html')

def user_register(request):
    return render(request, 'ecommerce/user/register.html')
	
def logout(request):
	# Clear the session cookies to logout the user. 
    django_logout(request)
	# Redirect after logout
    return HttpResponseRedirect('/ecommerce/user/login')