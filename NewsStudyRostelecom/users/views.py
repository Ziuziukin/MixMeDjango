from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def account(request):
    user_acc = Account.objects.get(user=request.user)
    context = {'user_info': user_acc,
               }
    return render(request, 'users/account.html', context=context)
