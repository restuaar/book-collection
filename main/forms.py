from django.forms import ModelForm
from main.models import Item

from django.contrib.auth.forms import UserCreationForm
# from django.forms.forms import Form

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]

# class RegisterForm(UserCreationForm):   
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password1', 'password2')