from django import forms
from .models import Profession, Human
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='e-mail',
                                widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields=('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()

class NewsForm(forms.ModelForm):

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match('r\d', name):
            raise ValueError('Заголовок не должен начинаться с цифр')
        return name

    class Meta:
        model = Human
        # fields ='__all__'
        fields = ['name', 'surname', 'date_birth', 'place_residence', 'is_published', 'profession']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'date_birth': forms.TextInput(attrs={
                'class': 'form-control',
                'rows': 5
            }),
            'place_residence': forms.TextInput(attrs={
                'class': 'form-control',
                'rows': 5
            }),
            'profession': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

# name = forms.CharField(max_length=150, label='Имя', widget=forms.TextInput(attrs={
#    'class': 'form-control'
# }))
# surname = forms.CharField(label='Фамилия', required=False, widget=forms.TextInput(attrs={
#    'class': 'form-control',
#    'rows': 5
# }))
# date_birth = forms.CharField(label='Адрес проживания', required=False, widget=forms.TextInput(attrs={
#    'class': 'form-control',
#    'rows': 5
# }))
# is_published = forms.BooleanField(label='Запомнить', initial=True)
# profession = forms.ModelChoiceField(queryset=Profession.objects.all(), label='Профессия', empty_label='Выберите профессию', widget=forms.Select(attrs={
#     'class': 'form-control'
# }))
