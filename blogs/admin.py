from django.contrib import admin
from .models import writer,post
# Register your models here.
@admin.register(writer)
class writerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user')
    search_fields = ('name', 'email')

@admin.register(post)
class postAdmin(admin.ModelAdmin):
   list_display=('text','date','title','writer', 'image')
   search_fields=('date','title')