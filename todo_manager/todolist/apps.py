from django.apps import AppConfig


class TodolistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todolist'
    verbose_name = 'ToDo List'
    app_label = 'todolist'