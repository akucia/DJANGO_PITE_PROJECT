from django.shortcuts import render
from datetime import datetime
from ..models import *
import string
import random
from dateutil import parser
from django.core.urlresolvers import reverse


def idGenerator(size=8, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def surveyAnswer(request):
    if 'userID' in request.GET.keys():
        try:
            row = Survey.objects.get(userID=request.GET['userID'])
        except:
            return render(request, "survey_answerID_panel.html",
                          {'errorMsg': 'Ankieta o podanym ID nie istnieje wprowadź poprawne ID.'})

        dateTimes = []

        for fromTime, toTime in row.fields:
            dateTimes.append((fromTime, toTime, False))

        name=""
        surname=""
        email=""
        answerID=None
        editURL=None

        if'answerID' in request.GET.keys():
            answerID=request.GET['answerID']
            try:
                answerRow = Answer.objects.get(answerID=request.GET['answerID'])
                name=answerRow.name
                surname=answerRow.surname
                email=answerRow.email

                for i in range(0,len(dateTimes)):
                    fromTime,toTime,*other=dateTimes[i]

                    if (fromTime,toTime) in answerRow.answer.keys():
                        dateTimes[i]=(fromTime,toTime,answerRow.answer[(fromTime,toTime)])

                editURL=request.build_absolute_uri(reverse('surveyAnswer'))+"?userID="+request.GET['userID']+"&answerID="+answerID
            except:
                pass

        return render(request, 'survey_answer_panel.html', {'title': row.title,
                                                            'creationDate': row.creation_date,
                                                            'description': row.description,
                                                            'dateTimes': dateTimes,
                                                            'userID': request.GET['userID'],
                                                            'answerID' : answerID,
                                                            'name' : name,
                                                            'surname' :surname,
                                                            'email' : email,
                                                            'editURL' : editURL,
                                                            })

    else:
        return render(request, "survey_answerID_panel.html")


def saveAnswer(request):
    if 'userID' in request.POST.keys():
        try:
            surveyRow = Survey.objects.get(userID=request.POST['userID'])


            answerID = None
            answerRow=None
            if 'answerID' in request.POST.keys():
                answerRow=Answer.objects.get(answerID=request.POST['answerID'])
                answerID=request.POST['answerID']
            else:
                answerRow = Answer()

                while True:
                    answerID = idGenerator()
                    try:
                        # make sure that adminID is unique
                        Answer.objects.get(answerID=answerID)
                    except:
                        break

                answerRow.answerID=answerID

            answerRow.survey = surveyRow
            answerRow.name = request.POST['name']
            answerRow.surname = request.POST['surname']
            answerRow.email = request.POST['email']

            listOfAnswers = dict()

            for field in request.POST.keys():
                if '|' in field:
                    try:
                        datesInString = field.split('|')
                        fromDate = parser.parse(datesInString[0])
                        toDate = parser.parse(datesInString[1])
                        answer = request.POST[field]
                        listOfAnswers[(fromDate), (toDate)] = answer
                    except:
                        pass

            listOfValidatedAnswers=dict()
            for element in surveyRow.fields:
                if element in listOfAnswers.keys():
                    listOfValidatedAnswers[element]=listOfAnswers[element]
                else:
                    listOfValidatedAnswers[element]=False

            answerRow.answer=listOfValidatedAnswers

            answerRow.save()

            return render(request,"redirector.html",{"newUrl" : "surveyAnswer?answerID="+answerID+"&userID="+request.POST['userID']+"&lastChanges=OK"})

        except:
            return render(request, "some_error_panel.html",
                          {'errorDescription': "Wystąpił błąd przy próbie zapisu odpowiedzi."})

    else:
        return render(request, "some_error_panel.html", {'errorDescription': "Nie otrzymano poprawnego zapytania."})
