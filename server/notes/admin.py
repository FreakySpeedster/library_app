from django.contrib import admin
from .models import Note
# Register your models here.

@admin.register(Note)
class noteAdmin(admin.ModelAdmin):
    list_display = ['title', 'topic', 'content', 'labels']
# Register your models here.
