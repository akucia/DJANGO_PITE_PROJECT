from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.shortcuts import render
from django.http import Http404
import re
from ..models import SurveyUser

from django.http import HttpResponse
import json

def registerAjaxRequest(request):
    if request.method == 'POST':
        try:
            fieldState=dict()

            allCorrect=True

            if not re.match(r"^[A-Za-z àáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ]{3,20}$",request.POST['name']):
                allCorrect=False
                fieldState["inputName"]="Imię musi składać się z 3-20 liter"

            if not re.match(r"^[A-Za-z àáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð,.'-]{3,50}$",request.POST['surname']):
                allCorrect=False
                fieldState['surnameInput']="Nazwisko musi składać się z 3-50 liter i znaków"

            if not re.match(r"^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$", request.POST['email']):
                allCorrect=False
                fieldState['inputEmail']="Wpisz e-mail w poprawnym formacie"

            if not re.match(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}",request.POST["password"]):
                allCorrect=False
                fieldState['inputPassword']="Hasło musi zawierać litery o różnej wielkości oraz cyfry i mieś długość co najmniej 6 znaków"

                if request.POST["password"]!=request.POST["rePassword"]:
                    allCorrect=False
                    fieldState['inputPassword']="Podane hasła nie są zgodne"
                    fieldState['inputPasswordRetype'] = "Podane hasła nie są zgodne"

            if allCorrect:
                row=SurveyUser(name=request.POST['name'],surname=request.POST['surname'],email=request.POST['email'])
                row.hash_of_password=make_password(request.POST['password'],salt=None,hasher='unsalted_md5')
                row.save()

                #auto login
                user = SurveyUser.objects.get(email=request.POST['email'])
                request.session['member_id'] = user.id
                request.session['member_name'] = user.name
                request.session['member_surname'] = user.surname

                return HttpResponse(
                    json.dumps({"fieldState": fieldState,
                                "successfullRegistration": True
                                }),
                    content_type="application/json"
                )

            else:
                return HttpResponse(
                    json.dumps({"fieldState": fieldState,
                                "successfullRegistration": False,
                                "errorMSG": "Wprowadzone dane są błędne"
                                }),
                    content_type="application/json"
                )


        except IntegrityError:
            fieldState['inputEmail'] = "Podany email istnieje"

            return HttpResponse(
                json.dumps({"fieldState": fieldState,
                            "successfullRegistration": False,
                            "errorMSG": "Podany email już istnieje"
                            }),
                content_type="application/json"
            )

        except:
            return HttpResponse(
                json.dumps({"fieldState": fieldState,
                            "successfullRegistration": False,
                            "errorMSG": "Nieobsługiwany błąd"
                            }),
                content_type="application/json"
            )

    else:
        return HttpResponse(
            json.dumps({"errorMSG": "Błąd metody przekazywania danych"}),
            content_type="application/json"
        )