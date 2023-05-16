from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader

from .forms import NewUserForm
from .models import Movie, Genre
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import login

from django.core.paginator import Paginator

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token


class IndexView(generic.ListView):
    template_name = 'userview/index.html'
    context_object_name = 'movies'
    paginate_by = 5

    def get_queryset(self):
        return Movie.objects.order_by('-title')


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


def index(request):
    movie_list = Movie.objects.order_by('-title')
    paginator = Paginator(movie_list, 5)  # Show 5 movies per page

    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)

    context = {
        'movies': movies
    }
    return render(request, 'userview/index.html', context)


def view_movie(request: HttpRequest, movie_id):
    response = 'you are looking at the movie with an id %s'
    return HttpResponse(response % movie_id)


def view_genre(request: HttpRequest, genre_id):
    response = 'you are looking at the genre with an id %s'
    return HttpResponse(response % genre_id)


@csrf_exempt
def my_view(request):
    return HttpResponse("Hello world")


@csrf_protect
def my_view(request):
    c = {}
    # ...
    return render(request, "a_template.html", c)


@requires_csrf_token
def my_view(request):
    c = {}
    # ...
    return render(request, "a_template.html", c)


def register_request(request):
    form = NewUserForm()
    return render(request=request, template_name="userview/register.html", context={"register_form": form})
    if request.method == "POST":
        form = NewUserForm(request.POST)
    if form.is_valid():
        user = form.save()
    login(request, user)
    messages.success(request, "Registration successful.")
    return redirect("userview:homepage")
    messages.error(request, "Unsuccessful registration. Invalidinformation.")
