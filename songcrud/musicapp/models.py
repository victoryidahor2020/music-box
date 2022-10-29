from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Artiste(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Song(models.Model):
    artiste = models.ForeignKey(Artiste, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    date_released = models.DateTimeField(default=timezone.now, null=True)
    likes = models.ManyToManyField(User, related_name='liked_songs')
    
    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.TextField(null=True)
    song = models.ForeignKey(Song, null=True, on_delete=models.CASCADE)
