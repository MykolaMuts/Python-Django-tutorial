from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
from .models import Movie, Genre
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'userview/index.html'
    context_object_name = 'movies'


def get_queryset(self):
    return Movie.objects.order_by('-title')


class MovieView(generic.DetailView):
    model = Movie
    template_name = 'userview/movie.html'


class GenreView(generic.DetailView):
    model = Genre
    template_name = 'userview/genre.html'


def index(request: HttpRequest):
    movies = Movie.objects.order_by('-title')
    template = loader.get_template('userview/index.html')
    context = {
        'movies': movies
    }
    return HttpResponse(template.render(context, request))


def view_movie(request: HttpRequest, movie_id):
    response = 'you are looking at the movie with an id %s'
    return HttpResponse(response % movie_id)


def view_genre(request: HttpRequest, genre_id):
    response = 'you are looking at the genre with an id %s'
    return HttpResponse(response % genre_id)



