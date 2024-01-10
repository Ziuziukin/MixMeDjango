from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import UpdateView

from .models import *
from .forms import LoginUserForm, RegistrationUserForm, ProfileUserForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm

#функция авторизации пользователя
def login_user(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    elif request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                print('зашли в except')
                form.add_error(None, "Неправильный пароль или логин")
    else:
        form = LoginUserForm()
    return render(request, 'users/login.html', {'form': form})

#функция выхода пользователя из приложения
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

#функция регистрации пользователя с автоматической авторизацией
def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    elif request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            #создаем пользователя в БД auth_user
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # создаем запись в БД users_account
            create_account = Account.objects.create(user_id=User.objects.get(username=form.cleaned_data['username']).id,
                                                    gender='НД',
                                                    account_image='account_images/default_user.jpg')

            #авторизуем пользователя
            user = authenticate(request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = RegistrationUserForm()
    return render(request, 'users/registration.html', {'form': form})

#функция отображения информации ЛК пользователя
# def account(request):
#     if not request.user.is_authenticated:
#         return redirect(reverse('login'))
#     else:
#         user_acc = Account.objects.get(user=request.user)
#         context = {'user_info': user_acc,
#                    }
#         return render(request, 'users/account.html', context=context)

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/account.html'


    def get_success_url(self):
        return reverse_lazy('account')

    def get_object(self, queryset=None):
        return self.request.user
