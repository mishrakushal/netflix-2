from django.urls import path
from .views import Home

appname = 'netflixapp'

urlpatterns = [
    path('', Home, name="home"),
]