from django.contrib.auth.forms import AuthenticationForm
from django import forms
# from users.models import User


# class UserLoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Введите имя', "autocomplete":"username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control input', 'placeholder': 'Введите пароль'})
    )

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']