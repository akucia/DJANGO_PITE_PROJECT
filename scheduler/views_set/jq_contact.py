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

from django.http import HttpResponse

import json
import re


class CaptchaTestForm(forms.Form):
    captcha = CaptchaField()


def jqContactForm(request):
    form = CaptchaTestForm()
    if 'member_id' in request.session:
        row = SurveyUser.objects.get(id=request.session['member_id'])
        return render(request, "jq_contact.html", {
            'fields': [
                ('contactName', 'Imię:', 'text', row.name, False),
                ('contactSurname', 'Nazwisko:', 'text', row.surname, False),
                ('contactEmail', 'Email:', 'text', row.email, False),
                ('contactTopic', 'Temat:', 'text', "", True)
            ],
            'form': form
        })
    else:

        return render(request, "jq_contact.html", {
            'fields': [
                ('contactName', 'Imię:', 'text', '', True),
                ('contactSurname', 'Nazwisko:', 'text', '', True),
                ('contactEmail', 'Email:', 'text', '', True),
                ('contactTopic', 'Temat:', 'text', "", True)
            ],
            'form': form
        })


def jqContactSentMailRequest(request):
    if request.method == 'POST':
        form = CaptchaTestForm(request.POST)

        email = request.POST['email']
        name = request.POST['name']
        surname = request.POST['surname']
        topic = request.POST['topic']
        text_message = request.POST['text']

        fieldState = dict()
        allCorrect = True

        if not re.match(
                r"^[A-Za-z àáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ]{3,20}$",
                name):
            allCorrect = False
            fieldState["contactName"] = "Imię musi składać się z 3-20 liter"

        if not re.match(
                r"^[A-Za-z àáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð,.'-]{3,50}$",
                surname):
            allCorrect = False
            fieldState['contactSurname'] = "Nazwisko musi składać się z 3-50 liter i znaków"

        if not re.match(
                r"^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$",
                email):
            allCorrect = False
            fieldState['contactEmail'] = "Wpisz e-mail w poprawnym formacie"

        if not re.match(
                r"^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$",
                email):
            allCorrect = False
            fieldState['contactEmail'] = "Wpisz e-mail w poprawnym formacie"

        if not topic.isprintable():
            allCorrect = False
            fieldState['contactTopic'] = "Korzysztaj tylko z znaków drukowalnych "

        if len(topic) < 3 or len(topic) > 50:
            allCorrect = False
            fieldState['contactTopic'] = "Długość tematu powinna być w zakresie [3,50]"

        if not text_message.isprintable():
            allCorrect = False
            fieldState['contactText'] = "Korzysztaj tylko z znaków drukowalnych "

        if len(text_message) < 5 or len(text_message) > 1000:
            allCorrect = False
            fieldState['contactText'] = "Długość tematu powinna być w zakresie [5,1000]"

        if not form.is_valid():
            return HttpResponse(
                json.dumps({
                    "fieldState": fieldState,
                    "errorMSG": "Błąd captcha",
                    "successful": False
                }),
                content_type="application/json"
            )

        if allCorrect == False:
            return HttpResponse(
                json.dumps({
                    "fieldState": fieldState,
                    "errorMSG": "Błąd wprowadzonych danych",
                    "successful": False
                }),
                content_type="application/json"
            )

        text_message = text_message + '\n\n' + 'This message was send by ' + name + ' ' + surname

        try:
            send_mail(
                topic,
                text_message,
                "jsstach@gmail.com",
                ['ksstach@gmail.com'],
                fail_silently=False,
            )
        except:
            return HttpResponse(
                json.dumps({
                    "errorMSG": "Błąd wysyłania danych",
                    "successful": False
                }),
                content_type="application/json"
            )

        return HttpResponse(
            json.dumps({"fieldState": fieldState,
                        "successful": True
                        }),
            content_type="application/json"
        )

    else:
        return HttpResponse(
            json.dumps({
                "errorMSG": "Błąd metody przekazywania danych",
                "successful": False
            }),
            content_type="application/json"
        )
