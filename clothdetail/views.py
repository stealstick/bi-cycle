from django.shortcuts import render
from django.http import HttpResponse
from main.models import Cloth
from mypage.models import Send

def index(request, cloth_name):
    try :
        rent = Cloth.objects.filter(lenter = request.user)
        #send = Send.objects.filter(resiver = resiver.user)       
    except:
        rent = None;
        #send = None;
    try :
        send = Send.objects.filter(resiver = request.user)
    except:
        send =None;
    cloth= Cloth.objects.get(cloth_name=cloth_name)
    context = {'cloth':cloth,
    'rent' : rent,
    'my_send': send,
    }
    return render(request, 'clothdetail/clothdetail.html', context)
# Create your views here.
