from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
def root(request):
    return redirect("/blogs")
def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/")
def show(request, id):
    return HttpResponse(f"localhost:8000/blogs/15 should display the message: 'placeholder to display blog number {id}",id)
def edit(request,id):
    return HttpResponse("placeholder to edit blog {id}")
def delete(request, id):
    return redirect ('/blogs')
def redirected_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})