from django.db import models

# Create your models here.
from django.urls import reverse


class CreateSurvey(models.Model):
    heading=models.CharField(max_length=100,null=True,blank=True)
    timer=models.IntegerField()

    question1 = models.CharField(max_length=200, null=True, blank=True)
    option1 = models.CharField(max_length=100, null=True, blank=True)
    option2 = models.CharField(max_length=100, null=True, blank=True)
    option3 = models.CharField(max_length=100, null=True, blank=True)
    option4 = models.CharField(max_length=100, null=True, blank=True)

    question2 = models.CharField(max_length=200, null=True, blank=True)
    option12 = models.CharField(max_length=100, null=True, blank=True)
    option22 = models.CharField(max_length=100, null=True, blank=True)
    option32 = models.CharField(max_length=100, null=True, blank=True)
    option42 = models.CharField(max_length=100, null=True, blank=True)

    question3 = models.CharField(max_length=200, null=True, blank=True)
    option13 = models.CharField(max_length=100, null=True, blank=True)
    option23 = models.CharField(max_length=100, null=True, blank=True)
    option33 = models.CharField(max_length=100, null=True, blank=True)
    option43 = models.CharField(max_length=100, null=True, blank=True)

    question4 = models.CharField(max_length=200, null=True, blank=True)
    option14 = models.CharField(max_length=100, null=True, blank=True)
    option24 = models.CharField(max_length=100, null=True, blank=True)
    option34 = models.CharField(max_length=100, null=True, blank=True)
    option44 = models.CharField(max_length=100, null=True, blank=True)

    question5 = models.CharField(max_length=200, null=True, blank=True)
    option15 = models.CharField(max_length=100, null=True, blank=True)
    option25 = models.CharField(max_length=100, null=True, blank=True)
    option35 = models.CharField(max_length=100, null=True, blank=True)
    option45 = models.CharField(max_length=100, null=True, blank=True)

    question6 = models.CharField(max_length=200, null=True, blank=True)
    option16= models.CharField(max_length=100, null=True, blank=True)
    option26 = models.CharField(max_length=100, null=True, blank=True)
    option36 = models.CharField(max_length=100, null=True, blank=True)
    option46 = models.CharField(max_length=100, null=True, blank=True)

    question7 = models.CharField(max_length=200, null=True, blank=True)
    option17 = models.CharField(max_length=100, null=True, blank=True)
    option27 = models.CharField(max_length=100, null=True, blank=True)
    option37 = models.CharField(max_length=100, null=True, blank=True)
    option47 = models.CharField(max_length=100, null=True, blank=True)

    question8 = models.CharField(max_length=200, null=True, blank=True)
    option18 = models.CharField(max_length=100, null=True, blank=True)
    option28 = models.CharField(max_length=100, null=True, blank=True)
    option38 = models.CharField(max_length=100, null=True, blank=True)
    option48 = models.CharField(max_length=100, null=True, blank=True)

    question9 = models.CharField(max_length=200, null=True, blank=True)
    option19 = models.CharField(max_length=100, null=True, blank=True)
    option29 = models.CharField(max_length=100, null=True, blank=True)
    option39 = models.CharField(max_length=100, null=True, blank=True)
    option49 = models.CharField(max_length=100, null=True, blank=True)

    question10 = models.CharField(max_length=200, null=True, blank=True)
    option10 = models.CharField(max_length=100, null=True, blank=True)
    option20 = models.CharField(max_length=100, null=True, blank=True)
    option30 = models.CharField(max_length=100, null=True, blank=True)
    option40 = models.CharField(max_length=100, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("create-view")