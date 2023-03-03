from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-input",
        'id': 'InputEmailAddress',
        'type': 'text',
        'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-input",
        'id': "InputPassword",
        'type': "password",
        'placeholder': "Введите пароль",
    }))

    class Meta:
        model = User
        fields = ['login', 'password']


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-input",
        'id': "InputFirstName",
        'type': "text",
        'placeholder': "Имя",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-input",
        'id': "InputLastName",
        'type': "text",
        'placeholder': "Фамилия",
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-input",
        'id': "InputEmailAddress",
        'type': "text",
        'placeholder': "Email",
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-input",
        'id': "InputUsername",
        'type': "text",
        'placeholder': "Никнейм",
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-input",
        'id': "InputPassword",
        'type': "password",
        'placeholder': "Пароль",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-input",
        'id': "InputConfirmPassword",
        'type': "password",
        'placeholder': "Подтверждение пароля",
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'readonly': True,
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'img-radius',
    }), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input username-input',
        'readonly': True,
    }))
    date_joined = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'class': 'form-input',
        'readonly': True,
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'image', 'username', 'date_joined']
