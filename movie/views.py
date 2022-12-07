from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Movie
# Create your views here.

class moveListView(ListView):
    template_name='movie/movie_list.html'
    model = Movie

class moveDetailView(DetailView):
    model = Movie
    template_name ='movie/movie_detail.html'
    

class MoveCreateView(CreateView):
   template_name = 'movie/movie_create.html'
   model = Movie
   fields= ['title','description','purchaser','img_url']
   success_url = reverse_lazy('movie_list')

class MovieUpdateView(UpdateView):
  template_name = 'movie/movie_update.html'
  model = Movie
  fields= ['title','description','purchaser','img_url']
  success_url = reverse_lazy('movie_list')

class MoveDeleteView(DeleteView):
    template_name = 'movie/movie_delete.html'
    model = Movie
  
    success_url = reverse_lazy('movie_list')