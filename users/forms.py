from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import *

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control login-input', 'placeholder': 'Логин'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control login-input', 'placeholder': 'Password'}))


class CustomUserCreationForm(UserCreationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control register-input',
                                      'placeholder': 'Введите имя пользователя'}))
    first_name = forms.CharField(label='Имя',
                          widget=forms.TextInput(
                              attrs={'class': 'form-control register-input', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(required=False,
                         widget=forms.TextInput(
                             attrs={'class': 'form-control register-input', 'placeholder': 'Введите фамилию'}))
    email = forms.CharField(required=False,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control register-input', 'placeholder': 'Введите Email'}))

    image = forms.FileField(label='Картинка',
                            widget=forms.FileInput(
                                attrs={'class': 'form-control form-control-lg'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control register-input',
                                                                  'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control register-input',
                                                                  'placeholder': 'Повторите пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'image', 'email']

