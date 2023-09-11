from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Todo
from django.urls import reverse_lazy


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["titulo", "deadline"]
    success_url = reverse_lazy("home")
