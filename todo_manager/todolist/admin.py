from django.contrib import admin

from .models import TodoItem

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = "id", "title", "done"
    list_display_links = "id", "title"