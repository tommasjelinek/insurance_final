from django import forms
from django.forms import ModelForm

from . models import Users
from . models import Contract
from . models import Product

# Create a User form
class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'email', 'address', 'phone',)
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'address': '',
            'phone': '',


        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Jmeno'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Prijmeni'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'address': forms.TextInput(attrs={'placeholder': 'Adresa'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon'}),



        }


# Create a Contract form
class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = ('product', 'amount', 'start_date', 'end_date')
        labels = {
            'product': 'Typ pojisteni',
            'amount': 'Castka',
            'start_date': 'Platne od',
            'end_date': 'Platne do',

        }

        widgets = {

            'product_name': forms.ModelMultipleChoiceField(queryset=Product.objects.all()),
            'amount': forms.TextInput(attrs={'placeholder': ''}),
            'start_date': forms.DateInput(format=('%d-%m-%Y'),attrs={'placeholder': '' 'Select a date', 'type': 'date'}),
            'end_date': forms.DateInput(format=('%d-%m-%Y'),attrs={'placeholder': '' 'Select a date', 'type': 'date'}),


        }


# Create a Product form
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('product_name',)

        labels = {
            'product_name': '',
        }

        widgets = {
            'product_name': forms.TextInput(attrs={'placeholder': 'Nazev produktu'}),

        }


