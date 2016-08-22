from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from ..models import SurveyUser
from django.http import HttpResponse

import json

def logoutRequestAjax(request):
    try:
        del request.session['member_id']
        del request.session['member_name']
        del request.session['member_surname']
    except KeyError:
        pass

    return HttpResponse(
        json.dumps({}),
        content_type="application/json"
    )

def loginRequestAjax(request):
    pass
