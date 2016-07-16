from django.shortcuts import render
from ..models import *


def htmlReport(request):
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

        return render(request,"html_report_template.html",
                      {'answerDates': listOfAnswers,
                           'title' : row.title ,
                           'description' : row.description,
                           'creationDate' : row.creation_date
                        })

    else:
        return render(request,"some_error_panel.html",{ 'errorDescription' : "Nie działa"})

