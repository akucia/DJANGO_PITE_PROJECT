from django.shortcuts import render
from datetime import datetime
from .models import *
import string
import random
from dateutil import parser
from django.core.urlresolvers import reverse

# Create your views here.
def main(request):
    return render(request, 'main.html')

def jqMain(request):
    return render(request,'jq_base.html')

def jqNavBar(request):
    return render(request,'jq_navBar.html')

def jqDefault(request):
    return render(request,'jq_main.html')

def jqLoginPane(request):
    return render(request,'jq_loginPane.html')

def jqRegisterPanel(request):
    return render(request,'jq_register_panel.html',{'fields': [
        ('inputName','Imię:','text'),
        ('inputSurname','Nazwisko:','text'),
        ('inputEmail','Email','text'),
        ('inputPassword','Hasło:','password'),
        ('inputPasswordRetype', 'Powtórz hasło:', 'password')
    ]})