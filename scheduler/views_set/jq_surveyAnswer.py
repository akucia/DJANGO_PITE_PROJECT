from django.shortcuts import render
from datetime import datetime , timedelta
from ..models import *
import string
import random
from dateutil import parser
from django.core.urlresolvers import reverse
from django.utils import timezone
import json
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse


def jq_surveyAnswer(request):
    return render(request, "jq_surveyAnswer.html")

def jqSurveyAnswerCheckUserIdRequest(request):
    if request.method=="POST":
        try:
            row = Survey.objects.get(userID=request.POST['userID'])

            return HttpResponse(
                json.dumps({
                    "success": True}),
                content_type="application/json"
            )
        except:
            return HttpResponse(
                json.dumps({
                    "success" : False,
                    "errorMSG": "Ankieta o podanym id nie istnieje"}),
                content_type="application/json"
            )
    else:
        return HttpResponse(
            json.dumps({
                "success": False,
                "errorMSG": "Błąd metody przekazywania danych"
            }),
            content_type="application/json"
        )

def jq_SurveyAnswerForm(request):
    if 'userID' in request.GET.keys():
        try:
            row = Survey.objects.get(userID=request.GET['userID'])
        except:
            return render(request, "jq_surveyAnswer.html")

        dateTimes = []

        for fromTime, toTime in row.fields:
            dateTimes.append((fromTime, toTime, False))

        name = ""
        surname = ""
        email = ""
        answerID = None
        editURL = None

        if 'answerID' in request.GET.keys():
            answerID = request.GET['answerID']
            try:
                answerRow = Answer.objects.get(answerID=request.GET['answerID'])
                name = answerRow.name
                surname = answerRow.surname
                email = answerRow.email

                for i in range(0, len(dateTimes)):
                    fromTime, toTime, *other = dateTimes[i]

                    if (fromTime, toTime) in answerRow.answer.keys():
                        dateTimes[i] = (fromTime, toTime, answerRow.answer[(fromTime, toTime)])

                editURL = request.build_absolute_uri(reverse('surveyAnswer')) + "?userID=" + request.GET[
                    'userID'] + "&answerID=" + answerID
            except:
                pass

        return render(request, 'jq_surveyAnswerForm.html', {'title': row.title,
                                                            'creationDate': row.creation_date,
                                                            'description': row.description,
                                                            'dateTimes': dateTimes,
                                                            'userID': request.GET['userID'],
                                                            'answerID': answerID,
                                                            'name': name,
                                                            'surname': surname,
                                                            'email': email,
                                                            'editURL': editURL,
                                                            })

    else:
        return render(request, "jq_surveyAnswer.html")

def jq_SurveyAnswerRedirector(request):
    if 'userID' in request.GET.keys():
        url=""
        if 'answerID' in request.GET.keys():
            url = "hidden/jqSurveyAnswerForm?userID=" + request.GET['userID'] + "&answerID=" + request.GET['answerID']
        else:
            url = "hidden/jqSurveyAnswerForm?userID=" + request.GET['userID']

        return render(request,"jq_base.html",{"loadPage":url})

    else:
        url = "hidden/jqSurveyAnswer"
        return render(request,"jq_base.html",{"loadPage":url})