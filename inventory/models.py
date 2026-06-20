import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    comments = models.TextField(null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def was_created_recently(self):
        return self.date_created >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return {self.name, self.email, self.role, self.date_created, self.last_modified}

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name