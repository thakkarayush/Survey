from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import CreateSurvey

class CreateNewSurvey(CreateView):
    model = CreateSurvey
    fields ='__all__'

class ListSurveyView(ListView):
    model = CreateSurvey
    context_object_name = 'CreateSurvey'
    template_name = "create/Survey_question.html"

class DeleteSurveyView(DeleteView):
    model = CreateSurvey
    success_url = 'create/view'

class DetailView(DetailView):
    model = CreateSurvey