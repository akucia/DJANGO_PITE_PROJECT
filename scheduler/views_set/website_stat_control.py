from django.shortcuts import render
from datetime import datetime, timedelta
from ..models import *
import string
import random
from dateutil import parser
from django.core.urlresolvers import reverse
from django.utils import timezone
import json


def websiteStatManager(request):
    userlist = SurveyUser.objects.all()
    numberOfUsers = len(userlist)
    recentusers = userlist.order_by('-sign_in_date')[:1]
    mostRecentUser = recentusers[0].name + ' ' + recentusers[0].surname

    surveylist = Survey.objects.all()
    numberOfSurveys = len(surveylist)

    recentsurvey = surveylist.order_by('-creation_date')[:1]
    mostRecentSurvey = recentsurvey[0].title

    answerlist = Answer.objects.all()
    numberOfAnswers = len(answerlist)
    ########dane do wykresu #####
    daynum = []
    daynum.append(['Dzien', 'Ilosc utworzonych ankiet w ciągu danej ilości dni'])
    for i in range(1, 11):
        recently = timezone.now() - timedelta(days=i)
        recentSurveys = Survey.objects.all().exclude(creation_date__gte=timezone.now()).filter(
            creation_date__gte=recently)
        daynum.append([str(i), len(recentSurveys)])
    json_list_s = json.dumps(daynum)

    daynum = []
    daynum.append(['Dzien', 'Ilosc utworzonych odpowiedzi w ciągu danej ilości dni'])
    for i in range(1, 11):
        recently = timezone.now() - timedelta(days=i)
        recentAnswers = Answer.objects.all().exclude(creation_date__gte=timezone.now()).filter(
            creation_date__gte=recently)
        daynum.append([str(i), len(recentAnswers)])
    json_list_a = json.dumps(daynum)

    daynum = []
    daynum.append(['Dzien', 'Ilosc zarejestrowanych uzytkownikow w ciągu danej ilości dni'])
    for i in range(1, 11):
        recently = timezone.now() - timedelta(days=i)
        recentUsers = SurveyUser.objects.all().exclude(sign_in_date__gte=timezone.now()).filter(
            sign_in_date__gte=recently)
        daynum.append([str(i), len(recentUsers)])
    json_list_u = json.dumps(daynum)

    recently = timezone.now() - timedelta(days=1)
    recentSurveys = Survey.objects.all().exclude(creation_date__gte=timezone.now()).filter(creation_date__gte=recently)
    recentAnswers = Answer.objects.all().exclude(creation_date__gte=timezone.now()).filter(creation_date__gte=recently)
    recentUsers = SurveyUser.objects.all().exclude(sign_in_date__gte=timezone.now()).filter(sign_in_date__gte=recently)
    rSt = len(recentSurveys)
    rAt = len(recentAnswers)
    rUt = len(recentUsers)
    return render(request, "global_statistics.html", {
        'numberOfUsers': numberOfUsers,
        'mostRecentUser': mostRecentUser,
        'numberOfSurveys': numberOfSurveys,
        'mostRecentSurvey': mostRecentSurvey,
        'numberOfAnswers': numberOfAnswers,
        'surveyPlot': json_list_s,
        'answerPlot': json_list_a,
        'userPlot': json_list_u,
        'numberOfUsersToday': rUt,
        'numberOfSurveysToday': rSt,
        'numberOfAnswersToday': rAt,
    })