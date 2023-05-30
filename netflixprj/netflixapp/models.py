from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES = {
    ('All', 'All'),
    ('Kids', 'Kids'),
}

MOVIE_CHOICES = {
    ('seasonal', 'Seasonal'),
    ('single', 'Single'),
}


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True)


class Profile(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=1000)
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=1000)
    description = models.CharField(blank=True, null=True, max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=MOVIE_CHOICES, max_length=10)
    video = models.ManyToManyField('Video')
    image = models.ImageField(upload_to='covers')
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)

    def __str__(self) -> str:
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to='movies')

    def __str__(self) -> str:
        return self.title
