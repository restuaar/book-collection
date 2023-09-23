from django.forms import ModelForm
from main.models import Item

from django import forms  
# from django.forms.forms import Form

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]

# class RegisterForm(ModelForm):  
#     class Meta:
#         model = User
#         fields = ["username", "password1", "password2"] 