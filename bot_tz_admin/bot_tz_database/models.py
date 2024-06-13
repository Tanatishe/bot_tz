from unicodedata import category
from django.db import models


class User(models.Model):

    name = models.CharField(max_length=50)

class Category(models.Model):

    name = models.CharField(max_length=50)

class Subcategory(models.Model):

    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) 


class Goods(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)    
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)    
    price = models.PositiveIntegerField()
    image = models.ImageField(null=True)



    


    
    
