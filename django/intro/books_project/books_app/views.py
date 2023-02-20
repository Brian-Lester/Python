from django.shortcuts import render, redirect
from time import gmtime, strftime,localtime
from .models import Book, Author
    
def index(request):
    context = {
        'books':Book.objects.all()
    }
    return render(request,'index.html', context)

def create_book(request):
    data={
        'title': request.POST['title'],
        'desc':request.POST['desc'],
    }
    Book.objects.create(**data)
    return redirect(index)

def view_book(request,id):
    context={
        "book":Book.objects.get(id=id),
        'author':Author.objects.all()
    }
    return render(request, 'view_book.html',context)

def create_realationship(request,id):
        a_id= request.POST['author']
        id=id
        this_book=Book.objects.get(id=id)
        this_book.Authors.add(Author.objects.get(id=a_id))
        return redirect(f'/view/book/{id}')

def authors(request):
    context={
        'authors': Author.objects.all()
    }
    return render (request, 'author_list.html',context)

def create_author(request):
    data={
        'first_name': request.POST['first_name'],
        'last_name':request.POST['last_name'],
        'notes':request.POST['notes'],
    }
    Author.objects.create(**data)
    return redirect(authors)

def view_author(request,id):
    context={
        "book":Book.objects.all(),
        'author':Author.objects.get(id=id)
    }
    return render(request, 'view_author.html',context)

def create_realationship1(request,id):
        b_id= request.POST['book']
        id=id
        this_book=Book.objects.get(id=b_id)
        this_book.Authors.add(Author.objects.get(id=id))
        return redirect(f'/view/author/{id}')
