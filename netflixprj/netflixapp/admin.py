from django.contrib import admin
from netflixapp.models import Movie, CustomUser, Video, Profile


# Register your models here.
admin.site.register(Movie)
admin.site.register(CustomUser)
admin.site.register(Video)
admin.site.register(Profile)
