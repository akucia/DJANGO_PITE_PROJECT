from django.db import models
from datetime import datetime

# Create your models here.


class SurveyUser(models.Model):
    name=models.CharField(max_length=50,blank=False)
    surname=models.CharField(max_length=50,blank=False)
    email=models.EmailField(unique=True,blank=False)
    sign_in_date=models.DateTimeField(default=datetime.now,blank=True)
    hash_of_password=models.TextField(blank=False)

    def __str__(self):
        return '{}'.format(self.email)

class Survey(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    user=models.ForeignKey(SurveyUser,on_delete=models.CASCADE)
    fields=models.TextField()
    creation_date=models.DateTimeField()
    userID=models.TextField()
    adminID=models.TextField()

class Answer(models.Model):
    survey=models.ForeignKey(Survey,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    email=models.EmailField()
    answer=models.TextField()


