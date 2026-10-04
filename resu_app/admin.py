from django.contrib import admin
from .models import ResuModel

@admin.register(ResuModel)
class ResuModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'resume', 'transcript', 'uploaded_at']
    list_filter = ['uploaded_at', ]