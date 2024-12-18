from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to="image/", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
