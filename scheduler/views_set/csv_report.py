from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from subprocess import Popen, PIPE
import os
import tempfile
from django.shortcuts import render
from ..models import *
import csv
import re


def csvReport(request):

    row=None
    if 'adminID' in request.GET.keys():
        adminID=request.GET['adminID']
        try:
            row=Survey.objects.get(adminID=request.GET['adminID'])
        except:
            return render(request,"some_error_panel.html",{ 'errorDescription' : "Podany przez Ciebie numer ID nie występuje w bazie ankiet" })

        listOfAnswers=[]
        answers=Answer.objects.filter(survey=row)

        for fromDate,toDate in row.fields:
            listOfMatches=[]
            for answer in answers:
                try:
                    if answer.answer[(fromDate,toDate)]:
                        listOfMatches.append((answer.name,answer.surname,answer.email))
                except:
                    pass
            listOfAnswers.append((fromDate,toDate,listOfMatches))

        response = HttpResponse(content_type='text/csv')

        response['Content-Disposition'] = "attachment; filename=report.csv"
        writer = csv.writer(response)

        writer.writerow([row.title])
        writer.writerow(["Od","Do","Imię","Nazwisko","Email"])
        for fromDate, toDate, fitUsers in listOfAnswers:
            writer.writerow([fromDate, toDate])
            for name, surname, email in fitUsers:
                writer.writerow([" ", " ", name, surname, email])

        return response
    else:
        return render(request,"some_error_panel.html",{ 'errorDescription' : "Nie działa"})
