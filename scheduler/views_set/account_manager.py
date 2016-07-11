from django.shortcuts import render
from datetime import datetime
from ..models import *
import string
import random
from dateutil import parser
from django.core.urlresolvers import reverse


def accountManager(request):
    if 'member_id' in request.session:
        try:
            row=SurveyUser.objects.get(id=request.session['member_id'])

            mySurveys=Survey.objects.filter(user=row)

            listOfSurveys=[]
            for survey in mySurveys:
                listOfSurveys.append((survey.title,survey.adminID,survey.userID))

            return render(request,'account_management.html',{'email' : row.email,
                                                             'signInDate' : row.sign_in_date,
                                                             'listOfSurveys' : listOfSurveys,
                                                             'hideLoginPanel' : True
                                                             })

        except:
            return render(request, "some_error_panel.html",
                          {'errorDescription': "Wystąpił błąd przy próbie wczytania danych konta."})

def removeElement(request):
    try:
        row=Survey.objects.get(adminID=request.GET['adminID'])
        user=SurveyUser.objects.get(id=request.session['member_id'])

        if user==row.user:
            row.delete()
    except:
        pass
    return render(request,"redirector.html",{"newUrl" : "./accountManager"})
