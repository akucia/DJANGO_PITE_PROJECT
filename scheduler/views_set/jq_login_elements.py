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
    if request.method == 'POST':
        fieldState=dict()

        try:
            user = SurveyUser.objects.get(email=request.POST['email'])
        except:
            fieldState["inputLoginEmail"]="Nieprawidłowy adres e-mail"
            return HttpResponse(
                json.dumps({"fieldState": fieldState,
                            "successfullLogin": False,
                            "errorMSG": "Błąd logowania"
                            }),
                content_type="application/json"
            )

        else:
            hashed = make_password(password=request.POST['password'],
                                   salt=None,
                                   hasher='unsalted_md5')
            if user.hash_of_password == hashed:
                request.session['member_id'] = user.id
                request.session['member_name'] = user.name
                request.session['member_surname'] = user.surname

                return HttpResponse(
                    json.dumps({
                                "fieldState": fieldState,
                                "successfullLogin": True
                                }),
                    content_type="application/json"
                )
            else:
                fieldState["inputLoginPassword"]="Błędne hasło"
                return HttpResponse(
                    json.dumps({"fieldState": fieldState,
                                "successfullLogin": False,
                                "errorMSG": "Błąd logowania"
                                }),
                    content_type="application/json"
                )

    else:
        return HttpResponse(
            json.dumps({"errorMSG": "Błąd metody przekazywania danych"}),
            content_type="application/json"
        )