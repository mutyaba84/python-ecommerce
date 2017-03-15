from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30)
    about = models.TextField()
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    excerpt = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    author = models.PositiveIntegerField()
    featured_image = models.CharField(max_length=300)

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()