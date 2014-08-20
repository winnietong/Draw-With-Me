from tastypie.fields import ToManyField, ToOneField
from tastypie.resources import ModelResource
from draw.models import User, Drawing


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = "user"


class DrawingResource(ModelResource):
    user = ToManyField(UserResource, "user", null=True, blank=True)

    class Meta:
        queryset = Drawing.objects.all()
        resource_name = "drawing"

