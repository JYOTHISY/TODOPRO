from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(ListView):
    model=Item
    template_name='TODOAPP/home.html'

class TaskCreateView(CreateView):
    model=Item
    template_name='TODOAPP/createtask.html'
    fields=["task","task_description"]
    success_url= reverse_lazy('home')

class TaskDetailView(DetailView):
    model= Item
    template_name='TODOAPP/taskdescription.html'

class TaskDeleteView(DeleteView):
    model = Item
    template_name='TODOAPP/delete.html'
    success_url = reverse_lazy('home')

class TaskSearchView(ListView):
    model = Item
    template_name= 'TODOAPP/home.html'
    queryset= Item.objects.all()

    def get_queryset(self):
        result = self.request.GET.get('search_term')
        return Item.objects.filter(task__icontains =result)

class TaskUpdateView(UpdateView):
    model=Item
    template_name='TODOAPP/update.html'
    fields=["task","task_description"]
    success_url= reverse_lazy('home')






