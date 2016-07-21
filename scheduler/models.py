from django.db import models
from datetime import datetime

from picklefield.fields import PickledObjectField


# Create your models here.

class SurveyUser(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)
    sign_in_date = models.DateTimeField(default=datetime.now, blank=True)
    hash_of_password = models.TextField(blank=False)

    def __str__(self):
        return '{email}'.format(email=self.email)


class Survey(models.Model):
    title = models.CharField(max_length=300,blank=False)
    description = models.TextField(blank=False)
    user = models.ForeignKey(SurveyUser, on_delete=models.CASCADE)
    fields = PickledObjectField(blank=False)
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    userID = models.CharField(max_length=10,blank=False)
    adminID = models.CharField(max_length=10,blank=False)
    active = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return '{email} => {title}'.format(email=self.user.email,title=self.title)



class Answer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    answerID = models.CharField(max_length=10, blank=False)
    answer = PickledObjectField(blank=False)
    creation_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return '{survey} => {email}'.format(survey=self.survey,email=self.email)