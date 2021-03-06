from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    about = models.TextField(null=True)

    def __unicode__(self):
        return u"{}".format(self.username)


class Drawing(models.Model):
    local_path = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    author = models.ManyToManyField(User, blank=True, null=True, related_name="author")
    follower = models.ManyToManyField(User, blank=True, null=True, related_name="follower")

