from django.contrib import admin
from .models import writer,post
# Register your models here.
@admin.register(writer)
class writerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user')
    search_fields = ('name', 'email') 
    