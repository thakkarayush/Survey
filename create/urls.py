from django.urls import path
from .views import *
urlpatterns=[
    path("new/",CreateNewSurvey.as_view(),name='create-new'),
    path("view/",ListSurveyView.as_view(),name='create-view')
]