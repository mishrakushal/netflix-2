from django.urls import path
from .views import Home, ProfileLists, ProfileCreate, MovieList, MovieDetails, PlayMovie

app_name = 'netflixapp'

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('profiles/', ProfileLists.as_view(), name="profile-list"),
    path('profiles/create/', ProfileCreate.as_view(), name="profile-create"),
    path('watch/<str:profile_id>/', MovieList.as_view(), name="movie-list"),
    path('watch/detail/<str:movie_id>/', MovieDetails.as_view(), name="movie-details"),
    path('watch/play/<str:movie_id>/', PlayMovie.as_view(), name="play-movie"),
]
