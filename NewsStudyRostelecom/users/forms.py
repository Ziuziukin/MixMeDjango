from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-input',
                                          'placeholder': 'Введите логин'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-input',
                                          'placeholder': 'Введите пароль'}))

class RegistrationUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
                                   attrs={'class': 'form-input',
                                          'placeholder': 'Введите логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
                                   attrs={'class': 'form-input',
                                          'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='И еще раз', widget=forms.PasswordInput(
                                   attrs={'class': 'form-input',
                                          'placeholder': 'Повторите пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password']
