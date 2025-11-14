from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ('title', 'created_by', 'created_at')
    list_display = ('title', 'created_by', 'created_at')
