from django.shortcuts import render,redirect
from time import gmtime, strftime,localtime
from .models import Dojos,Ninjas
    
def index(request):
    context = {
        'dojos': Dojos.objects.all(),
        'ninjas': Ninjas.objects.all()
    }
    return render(request,'index.html', context)

def create_dojo(request):
    data={
        'name': request.POST['name'],
        'city':request.POST['city'],
        'state': request.POST['state'],
        'desc':request.POST['desc']
    }
    Dojos.objects.create(**data)
    return redirect(index)

def create_ninja(request):
    data={
        'first_name':request.POST['first_name'],
        'last_name':request.POST['last_name'],
        'dojo':Dojos.objects.get(id=request.POST['dojo'])
    }
    Ninjas.objects.create(**data)
    return redirect(index)


