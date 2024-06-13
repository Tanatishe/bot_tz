from django.contrib import admin
from .models import User, Category, Goods


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Goods)

# Register your models here.
