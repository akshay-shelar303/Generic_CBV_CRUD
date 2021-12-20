from django.shortcuts import render
from .models import Laptop
from django.views.generic import CreateView,ListView,UpdateView,DeleteView



class LaptopCreateView(CreateView):
    model = Laptop
    fields = "__all__"
    success_url = '/laptop/show/'

class LaptopListView(ListView):
    model = Laptop


class LaptopUpdateView(UpdateView):
    model = Laptop
    fields = "__all__"
    success_url = '/laptop/show/'

class LaptopDeleteView(DeleteView):
    model = Laptop
    fields = "__all__"
    success_url = '/laptop/show/'

