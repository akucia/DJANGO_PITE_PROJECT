from django.shortcuts import render
from datetime import datetime
from .models import *
import string
import random
from dateutil import parser


# Create your views here.
def main(request):
    return render(request, 'main.html')

def idGenerator(size=8, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def surveyManager(request):
    if 'adminID' in request.GET.keys():
        try:
            row=Survey.objects.get(adminID=request.GET['adminID'])
        except:
            return render(request,"some_error_panel.html",{ 'errorDescription' : "Podany przez Ciebie numer ID nie występuje w bazie ankiet" })

        if(row.user.id!=request.session['member_id']):
            return render(request,"some_error_panel.html",{ 'errorDescription' : "Nie masz uprawnienień do edycji tej ankiety" })


        dateTimes=[]
        id1=0
        id2=1


        try:
            if row.fields is not None:
                for fromDate,toDate in row.fields:
                    dateTimes.append((id1,id2,fromDate,toDate))
                    id1=id1+2
                    id2=id2+2

        except:
            return render(request,"some_error_panel.html",{ 'errorDescription' : "Nie udało się wczytać informacji o wcześniejszych wyborach" })

        # Append extra 5 fields
        for i in range(0,5):
            dateTimes.append((id1,id2,None,None))
            id1=id1+2
            id2=id2+2

        lastOk=False
        if 'lastChanges' in request.GET.keys():
            if request.GET['lastChanges']=="OK":
                lastOk=True


        return render(request,"survey_manager_panel.html",{'title' : row.title ,
                                                           'description' : row.description,
                                                           'creationDate' : row.creation_date,
                                                           'userID' : row.userID,
                                                           'adminID' : row.adminID,
                                                           'fieldsDebug' : row.fields,
                                                           'lastOk' : lastOk,
                                                           'dateTimes' : dateTimes })

    else:
        dateTimes=[]
        id1=0
        id2=1

        # Create 10 fields
        for i in range(0,10):
            dateTimes.append((id1,id2,None,None))
            id1=id1+2
            id2=id2+2

        return render(request,"survey_manager_panel.html",{'dateTimes' : dateTimes })


def saveSurvey(request):
    row=None

    if 'adminID' in request.GET.keys():
        adminID=request.GET['adminID']

        try:
            row=Survey.objects.get(adminID=request.GET['adminID'])
        except:
            return render(request,"some_error_panel.html",{ 'errorDescription' : "Próba odwołania do nieistniejącego rekordu" })

        if(row.user.id!=request.session['member_id']):
            return render(request,"some_error_panel.html",{ 'errorDescription' : "Próba wykonania zapisu pomimo braku uprawnień" })


    else:
        if(request.session['member_id'] is None):
            return render(request,"some_error_panel.html",{ 'errorDescription' : "Próba wykonania zapisu bez logowania" })

        row=Survey()

        adminID_t=None

        while True:
            adminID_t=idGenerator()
            try:
                # make sure that adminID is unique
                Survey.objects.get(adminID=adminID_t)
            except:
                break

        row.adminID=adminID_t

        userID=None

        while True:
            userID=idGenerator()
            try:
                # make sure that adminID is unique
                Survey.objects.get(userID=userID)
            except:
                break

        row.userID=userID

    try:
        row.user=SurveyUser.objects.get(id=request.session['member_id'])
    except:
        return render(request,"some_error_panel.html",{ 'errorDescription' : "Próba wykonania zapisu dla nieistniejącego użytkownika" })

    try:
        row.title=request.POST['title']
        row.description=request.POST['description']

        dates=[]

        for key in request.POST.keys():
            try:
                if "dateTimeFrom" in key:
                    secondKey=key.replace("From","To")
                    fromDate=parser.parse(request.POST[key])
                    toDate=parser.parse(request.POST[secondKey])

                    if fromDate > toDate:
                        raise
                    #dates.append((datetime.now(),datetime.now()))
                    dates.append((fromDate,toDate))
            except:
                pass


        row.fields=dates
        row.save()

    except:
        return render(request,"some_error_panel.html",{ 'errorDescription' : "Błąd odczytu danych z POST" })

    return render(request,"redirector.html",{"newUrl" : "./surveyManager?adminID="+row.adminID+"&lastChanges=OK"})
# TODO zmien render tak aby odświeżał stronę a nie ładował main.html



