# from django.http import request
from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'netflixapp/index.html') 