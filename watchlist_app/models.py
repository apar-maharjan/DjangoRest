from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True , blank=True, null=True)
    updated = models.DateTimeField(auto_now=True , blank=True, null=True)
    platform = models.ForeignKey(Platform, blank=True, null=True, on_delete=models.CASCADE, related_name = 'movie_platform')

    def __str__(self):
        return self.name