from django.shortcuts import render
from django.http import HttpResponse
from main.models import Cloth
from .models import Send
import datetime

def index(request):
    my_cloth= Cloth.objects.filter(owner=request.user)
    rent = Cloth.objects.filter(lenter = request.user)
    send = Send.objects.filter(resiver = request.user)
    context = {'my_cloth': my_cloth,
    'rent' : rent,
    'my_send' : send,
    }
    return render(request, 'mypage/mypage.html', context)