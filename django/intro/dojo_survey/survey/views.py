from django.shortcuts import render
from time import gmtime, strftime,localtime
    
def index(request):
    return render(request,'index.html')

def show(request):
    context={
        'name':request.POST['name'],
        'location':request.POST['school'],
        'lang':request.POST['lang'],
        'comment':request.POST['comments']
    }
    return render(request, 'show.html',context)