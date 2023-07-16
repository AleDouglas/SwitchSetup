from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'email','first_name','last_name', 'is_staff']


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ['username','email', 'first_name','last_name', 'is_staff']