from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Cloth
from mypage.models import Send
from account.models import User
import datetime
def index(request):
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
    clothes = Cloth.objects.all()

    context = {'clothes': clothes,
    'rent' : rent,
    'my_send' : send,
    }
    return render(request, 'main/main.html', context)

def category(request, category):
    category_item= Cloth.objects.filter(category=category)

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
    context = {'category_item': category_item,
    'rent' : rent,
    'my_send' : send,
    'category' : category}

    return render(request, 'main/category.html', context)

def send(request, username):
    cloth_name = request.GET['item']
    context = {'username' : username,
    'cloth_name':cloth_name
    }

    return render(request, 'main/send.html', context)

def sending(request, username):
    cloth_name = request.GET['item']
    text = request.POST['text']
    cloth= Cloth.objects.get(cloth_name=cloth_name)
    resiver = User.objects.get(username=username)
    date=datetime.datetime.now()
    send = Send(cloth=cloth, resiver=resiver,owner=request.user, text=text, update_date=date)
    send.save()
    
    return render(request, 'main/sendfinish.html')

def borrow(request):
    owner = request.GET['owner']
    cloth = request.GET['cloth']
    lenter = request.GET['lenter']
    owner = User.objects.get(username=owner)
    cloth = Cloth.objects.get(cloth_name=cloth, owner=owner)
    lenter = User.objects.get(username=lenter)
    cloth.lenter = lenter
    cloth.save()
    send=Send.objects.filter(cloth=cloth, resiver=owner, owner=lenter)
    send.delete()
    return HttpResponseRedirect("/mypage/")

def delete(request):
    cloth_name= request.GET['cloth_name']
    delete_item= Cloth.objects.filter(owner =request.user, cloth_name=cloth_name)
    delete_item.delete()
    return HttpResponseRedirect("/mypage/")

def search(request):
    search = request.GET['search']
    search_item=search
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
    search = Cloth.objects.filter(cloth_name__contains=search)      
    context = {'search': search,
    'rent' : rent,
    'my_send' : send,
    'search_item' : search_item,
    }
    return render(request, 'main/search.html', context)

def returnitem(request):
    cloth_name= request.GET['cloth_name']
    delete_item= Cloth.objects.get(lenter =request.user, cloth_name=cloth_name)
    delete_item.lenter = None
    delete_item.save()
    return HttpResponseRedirect("/")