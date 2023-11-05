from django.contrib import admin
from .models import Notes

# Register your models here.
@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'date']