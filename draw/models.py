from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    about = models.TextField(null=True)

class Image(models.Model):
    image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    authors = models.ManyToManyField(User, blank=True, null=True, related_name='image')