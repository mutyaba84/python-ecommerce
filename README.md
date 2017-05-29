# Python E-commerce

![alt tag](http://carlofontanos.com/wp-content/uploads/2017/03/python-ecommerce-using-django-watermarked.jpg)

A starter template madule for creating complex e-commerce web applications. Developed using Django v1.10.6 with best practices in mind.

### YouTube Demo: 
[![Python E-commerce by Carlo Fontanos (Demo)](https://img.youtube.com/vi/DexPhKYuMcY/0.jpg)](https://www.youtube.com/watch?v=DexPhKYuMcY)

## Pages and Features included:
1. Home
2. Login
3. Register
4. Account
5. Add Product
6. Edit Product
7. Manage Products
8. Product List
9. Single Product View

## How do I get setup?
1. Make sure you have latest python installed in your computer, you can download python from here: 		
	+ https://www.tutorialspoint.com/django/django_environment.htm
2. Install django using pip:
	+ pip install Django==1.11.2
or get the latest version here: https://www.djangoproject.com/download/
3. Verify your installation, run the following command:
	+ python -m django –version
	
## Setting up a new project in Django
1. From your command line, navigate to where you want to save your projects, then create a new project:
	+ django-admin startproject myproject
2. Setup migrations
	+ Run python manage.py makemigrations to create migrations
	+ Run python manage.py migrate to apply those changes to the database.
3. Now that your project is created and configured make sure it’s working:
	+ python manage.py runserver
	+ Navigate to http://127.0.0.1:8000/ in your browser to view the application.
		+ By default, the runserver command starts the development server on the internal IP at port 8000.
		+ if you want to change the port, syntax is:
			+ python manage.py runserver 8080
			+ where 8080 is the different port.
	+ if you want to share your project to other computers connected to the network, start the server like this:
		+ python manage.py runserver 192.168.2.75:8000
		+ Where 192.168.2.75 is your computer IP
	+ You can quit the server with CONTROL-C.

## Contribution guidelines
If you are a developer and you would like to contribute to this project, please follow my guidelines bellow:
- ALWAYS start a new branch before making changes to the codes
- Pull requests directly to the master branch will be ignored!
- Use a git client, preferably Source Tree or you can use git commands from your terminal, your choice!
- Many smaller commits are better than one large commit. Edit your file(s), if the edit does not break the code with things like syntax errors, commit. It is easier to reconcile many smaller commits than one large commit.
- When your feature or bug fix is ready, perform a pull request and notify carl.fontanos@gmail.com that your code is ready for review on Github.

## Author
### Carl Victor C. Fontanos
+ Website: [carlofontanos.com](http://www.carlofontanos.com)
+ Linkedin: [ph.linkedin.com/in/carlfontanos](http://ph.linkedin.com/in/carlfontanos)
+ Facebook: [facebook.com/carlo.fontanos](http://facebook.com/carlo.fontanos)
+ Twitter: [twitter.com/carlofontanos](http://twitter.com/carlofontanos)
+ Google+: [plus.google.com/u/0/107219338853998242780/about](https://plus.google.com/u/0/107219338853998242780/about)
+ GitHub: [github.com/carlo-fontanos](https://github.com/carlo-fontanos)

