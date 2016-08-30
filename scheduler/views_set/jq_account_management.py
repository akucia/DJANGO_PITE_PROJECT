from django.shortcuts import render
from datetime import datetime, timedelta
from ..models import *
import string
import random
from dateutil import parser
from django.core.urlresolvers import reverse
from django.utils import timezone
import json
from django.contrib.auth.hashers import make_password


def jqAccountManagement(request):
    if 'member_id' in request.session:

        # user Info
        userObject = SurveyUser.objects.get(id=request.session['member_id'])

        # list of surveys
        mySurveys = Survey.objects.filter(user=userObject)
        listOfSurveys = list()
        for survey in mySurveys:
            listOfSurveys.append((survey.title, survey.adminID, survey.userID))

        # user activity

        numberOfSurveys = len(mySurveys)
        recently = timezone.now() - timedelta(days=30)
        recentSurveys = Survey.objects.filter(user=userObject).exclude(creation_date__gte=timezone.now()).filter(
            creation_date__gte=recently)
        numberOfRecentS = len(recentSurveys)
        daySinceRegister = timezone.now() - userObject.sign_in_date
        daySinceRegister = int(daySinceRegister.total_seconds() / 3600 / 24)

        try:
            mostRecentSurvey = Survey.objects.filter(user=userObject).order_by('-creation_date')[:1]
            mostRecentSurvey = mostRecentSurvey[0].creation_date
        except:
            mostRecentSurvey = "Nie dodałeś jeszcze żadnej ankiety!"

        daynum = []
        daynum.append(['Dzien', 'Ilosc utworzonych ankiet'])
        for i in range(1, 11):
            recently = timezone.now() - timedelta(days=i)
            recentSurveys = Survey.objects.filter(user=userObject).exclude(
                creation_date__gte=timezone.now()).filter(
                creation_date__gte=recently)
            daynum.append([str(i), len(recentSurveys)])
        json_list = json.dumps(daynum)
        dateTimes = []
        id1 = 0
        id2 = 1
        dateTimes.append((id1, id2, None, None))

        return render(request, 'jq_account_management.html', {'email': userObject.email,
                                                              'listOfSurveys': listOfSurveys,
                                                              'signInDate': userObject.sign_in_date,
                                                              'hideLoginPanel': True,
                                                              'swap_LoginPanel_to_accountmanager_menu': True,
                                                              'daySinceRegister': daySinceRegister,
                                                              'mostRecentSurvey': mostRecentSurvey,
                                                              'numberOfSurveys': numberOfSurveys,
                                                              'numberOfRecentS': numberOfRecentS,
                                                              'plotData': json_list,
                                                              'dateTimes': dateTimes,
                                                              'website_type': 'userInfo',
                                                              })
