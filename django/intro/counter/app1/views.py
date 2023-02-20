

from django.shortcuts import render, redirect
from time import gmtime, strftime,localtime
    
def index(request):
    if 'count' not in  request.session:
        request.session ['count']= 1
        context ={
            'count': request.session ['count']
        }
    else:
        request.session['count']+=1
        context ={
            'count': request.session ['count']
        }
    return render(request,'index.html',context)

def destroy(request):
    del request.session['count']
    return redirect('/')

def plus2(request):
    request.session['count']+=1
    return redirect('/')

def plusnum(request):
    if request.method == "POST":
        request.session['count'] =int(request.POST['plusnum']) -1 + request.session['count']
        return redirect('/')
