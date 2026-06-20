from django.contrib import admin

from .models import Role, User, Category, Item

# Register your models here.
admin.site.register([Role, User, Category, Item])
