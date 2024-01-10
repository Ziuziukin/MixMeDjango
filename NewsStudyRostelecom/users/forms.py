from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

#форма для авторизации пользователя
class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-input',
                                          'placeholder': 'Введите логин'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-input',
                                          'placeholder': 'Введите пароль'}))

#форма для регистрации пользователя
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

    #проверка паролей на совпадение
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password']


#форма для обновления данных пользователя
# class UserUpdateForm(forms.ModelForm):
#
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'image']
#
#
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Account
#         fields = ['image']

class ProfileUserForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name']
        labels = {'first_name': 'Имя',
                  'last_name': 'Фамилия'}

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'})
        }
