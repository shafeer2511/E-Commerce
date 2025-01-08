from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter your username"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter your email"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter your password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Re-Enter the password"}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']