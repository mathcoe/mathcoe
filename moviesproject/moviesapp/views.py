from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movies
from .forms import MovieForms

# Create your views here.
def index(request):
    movie=Movies.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)
def details(request,movie_id):
    movie=Movies.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie})
def add_movies(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        discription = request.POST.get('discription',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movies=Movies(name=name, discription=discription,year=year,img=img)
        movies.save()


    return render(request,'add.html')

def update(request,id):
    movie=Movies.objects.get(id=id)
    form=MovieForms(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':movie,'form':form})

def delete(request,id):
    if request.method=='POST':
        movie=Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')