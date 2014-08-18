from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from draw.api.resources import UserResource, DrawingResource
from tastypie.api import Api

admin.autodiscover()

v1_api = Api(api_name="v1")
v1_api.register(UserResource())
v1_api.register(DrawingResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app_name.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(v1_api.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'draw.views.home', name='home'),

    # Save image to local
    url(r'^save_image/$', 'draw.views.save_image', name='save_image'),

    # LOGIN AND LOGOUT
    url(r'^register/$', 'draw.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),

    # USER AUTHENTICATION #
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    # Profile page ... domain/username
    url(r'^(?P<profile_username>[-\w\ !.]+)/$', 'draw.views.profile', name='profile'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
