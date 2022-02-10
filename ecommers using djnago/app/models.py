from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    p_name=models.CharField(max_length=50,null=True,blank=True)
    brand=models.CharField(max_length=50,null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='app/images/',null=True)
    
    def __str__(self):
        return self.p_name

class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    # post = models.ForeignKey(post, on_delete=models.CASCADE, null=False)
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    Reviewer=models.CharField(max_length=50,null=True,blank=True)
    rating=models.IntegerField(null=True,blank=True,default=0)
    comment=models.TextField(max_length=200,null=True,blank=True)
    # review_at=models.DateField(null=True)

    def __str__(self):
        return self.Reviewer


   