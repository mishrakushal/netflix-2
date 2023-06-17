from django.urls import path
from .views import Home, ProfileLists, ProfileCreate

app_name = 'netflixapp'

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('profiles/', ProfileLists.as_view(), name="profile-list"),
    path('profiles/create/', ProfileCreate.as_view(), name="profile-create"),
]