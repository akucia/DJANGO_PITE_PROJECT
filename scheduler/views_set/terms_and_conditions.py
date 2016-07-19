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


class CaptchaTestForm(forms.Form):
    captcha = CaptchaField()


def contactManager(request):
    form = CaptchaTestForm()
    if 'member_id' in request.session:
        row = SurveyUser.objects.get(id=request.session['member_id'])
        return render(request, "contact.html", {'email': row.email, 'form': form
                                                })
    else:
        return render(request, "contact.html", {'form': form})


def sendMail(request):
    if request.POST['respond'] == 'captcha':
        return contactManager(request)
    form = CaptchaTestForm(request.POST)
    if form.is_valid():
        email = request.POST['email']
        name = request.POST['name']
        surname = request.POST['surname']
        topic = request.POST['topic']
        text_message = request.POST['text']
        text_message = text_message + '\n' + 'This message was send by ' + name + ' ' + surname
        try:
            send_mail(
                topic,
                text_message,
                email,
                ['to@example.com'],
                fail_silently=False,
            )
        except:
            pass
        form = CaptchaTestForm()
        if 'member_id' in request.session:
            row = SurveyUser.objects.get(id=request.session['member_id'])
            return render(request, "contact.html", {'email': row.email, 'form': form, 'lastOk': True
                                                    })
        else:
            return render(request, "contact.html", {'form': form, 'lastOk': True,})
    else:
        if 'member_id' in request.session:
            row = SurveyUser.objects.get(id=request.session['member_id'])
            return render(request, "contact.html", {
                'email': row.email,
                'form': form,
                'lastOk': False,

            })
        else:
            return render(request, "contact.html", {'form': form, 'lastOk': False})