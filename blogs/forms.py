from django.contrib.auth.forms import AuthenticationForm
from django import forms

from django.contrib.auth.models import User
from .models import Profile

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        # widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Введите имя', "autocomplete":"username"})
        widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Введите имя', "autocomplete":"username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control input', 'placeholder': 'Введите пароль'})
    )


class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    photo = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['photo']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = self.instance.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            profile.save()
        return profile