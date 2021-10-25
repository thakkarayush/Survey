from django.db import models
from django import forms
# Create your models here.
from django.urls import reverse


class Login(models.Model):
    name=models.CharField(max_length=30,default="none")
    email=models.EmailField()
    password=models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse("login-view")