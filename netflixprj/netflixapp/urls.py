from django.urls import path
from .views import Home

appname = 'netflixapp'

urlpatterns = [
    path('', Home.as_view(), name="home"),
]