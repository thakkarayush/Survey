from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import Login
# Create your views here.
class NewLoginView(CreateView):
    model = Login
    fields = "__all__"

class ListLoginView(CreateView):
    model = Login
    fields = "__all__"
    #context_object_name = 'Login'
    template_name = 'login/register.html'