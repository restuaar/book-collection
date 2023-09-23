from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class Item(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    # rating = models.IntegerField()
    # type = models.CharField()

# class User(AbstractUser):
#     username = models.CharField(min_length=5, max_length=150)