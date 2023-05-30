from django.urls import path

from . import views

app_name = 'userview'

urlpatterns = [
    # path("genre/<int:genre_id>", views.view_genre, name="index"),
    # path("movie/<int:movie_id>", views.view_movie, name="index"),
    # path("", views.IndexView.as_view(), name="index"),
    path("", views.index, name="index"),
    path("genre/<int:pk>", views.GenreView.as_view(), name="genre"),
    path("movie/<int:pk>", views.MovieView.as_view(), name="movie"),
    path("register", views.register_request, name="register"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('movies/', views.movies_page, name='movies'),
    path('movies/rate/<int:movie_id>/', views.rate_movie, name='rate_movie'),
]
