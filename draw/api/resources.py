from django.db.models import Count
from tastypie.fields import ToManyField, ToOneField
from tastypie.resources import ModelResource
from draw.models import User, Drawing


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = "user"
        allowed_methods = ['get']


class DrawingResource(ModelResource):
    follower = ToManyField(UserResource, "follower", null=True, blank=True)
    author = ToManyField(UserResource, "author", null=True, blank=True)


    class Meta:
        queryset = Drawing.objects.annotate(follower_count=Count('follower')).order_by('-follower_count')
        resource_name = "drawing"
        allowed_methods = ['get', 'post']

    def dehydrate_author(self, bundle):
        for author in bundle.obj.author.all():
            print author.username
        return author

    def dehydrate_follower(self, bundle):
        follower_count = bundle.obj.follower.count()
        return follower_count