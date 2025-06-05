from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import TodoItem

def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = TodoItem.objects.all()
    return render(request, 'todolist/index.html', context={
        'todo_items': todo_items,
    })

class TodoListIndexView(ListView):
    template_name = 'todolist/index.html'
    model = TodoItem
    queryset = TodoItem.objects.all()

class TodoListView(ListView):
    model = TodoItem

class TodoListDoneView(ListView):
    queryset = TodoItem.objects.filter(done=True).all()

class TodoDetailView(DetailView):
    model = TodoItem