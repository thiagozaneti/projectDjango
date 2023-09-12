from django.shortcuts import render, get_object_or_404, redirect
from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Todo
from django.urls import reverse_lazy


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["titulo", "deadline"]
    success_url = reverse_lazy("home")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["titulo", "deadline"]
    success_url = reverse_lazy("home")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("home")


class TodoCompleteView(View):
    def get(self, request, pk): ##busca com o get 
        todo = get_object_or_404(Todo, pk = pk)
        todo.finished_at = date.today()
        todo.save() ##salva no banco o dia que a task foi feita
        return redirect("home")
