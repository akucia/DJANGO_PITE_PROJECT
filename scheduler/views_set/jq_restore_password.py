from django.shortcuts import render
from datetime import datetime, timedelta
from ..models import *
import string
import random
from dateutil import parser
from django.core.urlresolvers import reverse
from django.utils import timezone

import json
from django.core.mail import send_mail
from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.hashers import make_password

from django.http import HttpResponse

import json
import re

def jqRestorePassword(request):
    return render(request, 'jq_restore_password.html')

def jqSentRestoreEmailRequest(request):
    if request.method == 'POST':
        try:
            user = SurveyUser.objects.get(email=request.POST['email'])
        except:
            return HttpResponse(
                json.dumps({
                    "emailMessage": "Podany email nie został odnaleziony.",
                    "errorMSG": "Błąd danych wejściowych.",
                    "success": False
                }),
                content_type="application/json"
            )

        code = ""
        while len(code) != 6:
            i = random.randint(48, 90)
            while i > 57 and i < 65:
                i = random.randint(48, 90)
            code = code + chr(i)

        email = request.POST['email']

        try:
            send_mail(
                'PITE zmiana hasła',
                'Prosiłeś o zmianę hasła. Wygenerowany kod to :' + code,
                'jsstach@gmail.com',
                [email],
                fail_silently=False,
            )
        except:
            return HttpResponse(
                json.dumps({
                    "emailMessage": "Nie udało się wysłać maila. Spróbuj ponownie.",
                    "errorMSG": "Błąd wysyłania wiadomości.",
                    "success": False
                }),
                content_type="application/json"
            )

        request.session['restore_email'] = email
        request.session['restore_code'] = code


        return HttpResponse(
            json.dumps({
                "emailMessage": "Wiadomość została pomyślnie wysłana.",
                "success": True
            }),
            content_type="application/json"
        )

    else:
        return HttpResponse(
                json.dumps({"errorMSG": "Błąd metody przekazywania danych"}),
                content_type="application/json"
            )

def jqSentNewPasswordRequest(request) :
    if request.method == 'POST':
        fields=dict()
        allOk=True

        if request.POST['secretCode']!=request.session['restore_code']:
            fields["secretCode"]="Błędny kod weryfikujący"
            allOk=False

        if request.POST['restorePassword']!=request.POST['restorePasswordRetype']:
            fields["restorePassword"] = "Hasła nie są zgodne"
            fields["restorePasswordRetype"]=""
            allOk = False

        if not re.match(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}", request.POST["restorePassword"]):
            allOk = False
            fields['restorePassword'] = "Hasło musi zawierać litery o różnej wielkości oraz cyfry i mieć długość co najmniej 6 znaków"
            fields["restorePasswordRetype"] = ""
        if allOk:
            user=SurveyUser.objects.get(email=request.session['restore_email'])
            user.hash_of_password=make_password(request.POST['restorePassword'],salt=None,hasher='unsalted_md5')
            user.save()

            del request.session['restore_email']
            del request.session['restore_code']

            return HttpResponse(
                json.dumps({
                    "success": True
                }),
                content_type="application/json"
            )

        else:
            return HttpResponse(
                json.dumps({
                    "success": False,
                    "errorMSG": "Błąd wprowadzonych danych",
                    "fields": fields
                }),
                content_type="application/json"
            )
        pass
    else:
        return HttpResponse(
            json.dumps({
                "success": False,
                "errorMSG": "Błąd metody przekazywania danych"}),
            content_type="application/json"
        )