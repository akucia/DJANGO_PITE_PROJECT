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
from django.http import HttpResponse
import re


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


def jqAccountChangeUserdataRequest(request):
    if 'member_id' in request.session and request.method == 'POST':

        allCorrect = True
        fields = dict()

        if not re.match(
                r"^[A-Za-z àáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ]{3,20}$",
                request.POST['name']):
            allCorrect = False
            fields["changeNameInput"] = "Imię musi składać się z 3-20 liter"

        if not re.match(
                r"^[A-Za-z àáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð,.'-]{3,50}$",
                request.POST['surname']):
            allCorrect = False
            fields['changeSurnameInput'] = "Nazwisko musi składać się z 3-50 liter i znaków"

        if allCorrect:
            try:

                user = SurveyUser.objects.get(id=request.session['member_id'])
                user.name = request.POST['name']
                user.surname = request.POST['surname']
                user.save()
                request.session['member_name'] = user.name
                request.session['member_surname'] = user.surname

                return HttpResponse(
                    json.dumps({
                        "success": True,
                    }),
                    content_type="application/json"
                )

            except:
                return HttpResponse(
                    json.dumps({
                        "fields": {'changeNameInput': 'Błąd wprowadzania danych', 'changeSurnameInput': ''},
                        "success": False,
                        "errorMSG": "Błąd wprowadzania danych (spróbuj ponownie)"}),
                    content_type="application/json"
                )
        else:
            return HttpResponse(
                json.dumps({
                    "fields": fields,
                    "success": False,
                    "errorMSG": "Błąd podanych danych"}),
                content_type="application/json"
            )
    else:
        return HttpResponse(
            json.dumps({
                "success": False,
                "errorMSG": "Błąd metody przekazywania danych"}),
            content_type="application/json"
        )


def jqAccountChangeUserPasswordRequest(request):
    if 'member_id' in request.session and request.method == 'POST':
        fields = dict()
        allCorrect = True

        if request.POST["newPassword"] != request.POST["newPasswordRetype"]:
            allCorrect = False
            fields['changeNewPasswordInput'] = ""
            fields['changeNewPasswordRetypeInput'] = "Hasła muszą być zgodne"
        if not re.match(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}", request.POST["newPassword"]):
            allCorrect = False
            fields[
                'changeNewPasswordInput'] = "Hasło musi zawierać litery o różnej wielkości oraz cyfry i mieś długość co najmniej 6 znaków"

        user = SurveyUser.objects.get(id=request.session['member_id'])
        oldpass = make_password(password=request.POST['oldPassword'], salt=None, hasher='unsalted_md5')

        if oldpass != user.hash_of_password:
            allCorrect = False
            fields['changeOldPasswordInput'] = "Błędne hasło"

        if allCorrect:
            try:
                user.hash_of_password = make_password(password=request.POST['newPassword'], salt=None,
                                                      hasher='unsalted_md5')
                user.save()

                return HttpResponse(
                    json.dumps({
                        "success": True,
                    }),
                    content_type="application/json"
                )

            except:
                return HttpResponse(
                    json.dumps({
                        "fields": {"newPassword": "Błąd wprowadzania danych spróbuj ponownie",
                                   "changeNewPasswordInput": "",
                                   "changeNewPasswordRetypeInput": ""
                                   },
                        "success": False,
                        "errorMSG": "Błąd wprowadzania hasła"}),
                    content_type="application/json"
                )

        else:
            return HttpResponse(
                json.dumps({
                    "fields": fields,
                    "success": False,
                    "errorMSG": "Błąd wprowadzania hasła"}),
                content_type="application/json"
            )

    else:
        return HttpResponse(
            json.dumps({
                "success": False,
                "errorMSG": "Błąd metody przekazywania danych"}),
            content_type="application/json"
        )

def jqAccountRemoveSurveyRequest(request):
    if 'member_id' in request.session and request.method == 'POST':
        try:
            row = Survey.objects.get(adminID=request.POST['adminID'])
            user = SurveyUser.objects.get(id=request.session['member_id'])

            if user == row.user:
                row.delete()

            return HttpResponse(
                json.dumps({
                    "success": True}),
                content_type="application/json"
            )

        except:
            pass

    return HttpResponse(
        json.dumps({
            "success": False,
            "errorMSG": "Błąd usuwania"}),
        content_type="application/json"
    )