from django.urls import path
from .views import *
urlpatterns=[
    path("new/",NewLoginView.as_view(),name="login-new"),
    path("view/",ListLoginView.as_view(),name="login-view")
]