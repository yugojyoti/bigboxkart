from django import forms 
from .models import Customer,Cart,Product
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import password_validation

class MyRegistrationForm(UserCreationForm):
    email=forms.CharField(label="Email",widget=forms.EmailInput(attrs={"class":"form-control"})) 
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        widgets={"username":forms.TextInput(attrs={"class":"form-control"}),
      
        }

class MyLoginForm(AuthenticationForm):
    username=UsernameField(label=_("Username"), widget=forms.TextInput(attrs={'autofocus':True, "class":"form-control"}))
    password=forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={"autocomplete":'current-password',"class":"form-control"}))

class MyCustomerForm(forms.ModelForm):
    
    class Meta:
        model=Customer
        fields=["name","locality","city","state","zipcode","phone_number"]
        labels={"phone_number":"Phone Number"}
        widgets={
        "name":forms.TextInput(attrs={"class":"form-control"}),
        "locality":forms.TextInput(attrs={"class":"form-control"}),
        "city":forms.TextInput(attrs={"class":"form-control"}),
        "state":forms.Select(attrs={"class":"form-control"}),
        "zipcode":forms.NumberInput(attrs={"class":"form-control"}),
        "phone_number":forms.NumberInput(attrs={"class":"form-control"})}


class MyPasswordChangeForm(PasswordChangeForm):

    old_password=forms.CharField(label=_("Old Password"), strip=False, 
    widget=forms.PasswordInput(attrs={"autofocus":True, "class":'form-control'}))

    new_password1=forms.CharField(label=_('New Password'), strip=False, 
    widget=forms.PasswordInput(attrs={"autocomplete":'new-password',"class":"form-control"}),
    help_text=password_validation.password_validators_help_text_html())

    new_password2=forms.CharField(label=_("Confirm New Password"),strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete":'new-password',"class":"form-control"}))