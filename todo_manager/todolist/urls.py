from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'todolist'
urlpatterns = [
    # path('', views.TodoListIndexView.as_view(), name='index'),
    path('', views.TodoListIndexView.as_view(), name='index'),
    path('list/', views.TodoListView.as_view(), name='list'),
    path('done/', views.TodoListDoneView.as_view(), name='done'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='detail'),
]