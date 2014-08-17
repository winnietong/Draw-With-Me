from django.contrib import admin
from models import *

# Register your models here.

class DrawingAdmin(admin.ModelAdmin):
    list_display = ('title', 'local_path')
    list_filter = ('title', 'author')


admin.site.register(User)
admin.site.register(Drawing, DrawingAdmin)