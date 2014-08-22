from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    about = models.TextField(null=True)

    def __unicode__(self):
        return u"{}".format(self.username)


class Drawing(models.Model):
    local_path = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    # related_names would make more sense as something like authored_drawings and followed_drawings
    # you'd have a user object and would want to say get all of the drawings for this user where they're the author
    # user.authored_drawings
    author = models.ManyToManyField(User, blank=True, null=True, related_name="author")
    follower = models.ManyToManyField(User, blank=True, null=True, related_name="follower")

