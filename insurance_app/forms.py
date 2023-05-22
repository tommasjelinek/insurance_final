from django import forms
from django.forms import ModelForm
from . models import Users


# Create a User form

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'email', 'address', 'phone')



