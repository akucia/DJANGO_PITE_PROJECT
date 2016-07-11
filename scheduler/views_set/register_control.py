from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.shortcuts import render
from ..models import SurveyUser


def registerView(request):
    return render(request,"register_panel.html",{'hideLoginPanel' : True})


def registerRequest(request):
    try:
        row=SurveyUser(name=request.POST['name'],surname=request.POST['surname'],email=request.POST['email'])
        row.hash_of_password=make_password(request.POST['password'],salt=None,hasher='unsalted_md5')
        row.save()


        #auto login
        user = SurveyUser.objects.get(email=request.POST['email'])
        request.session['member_id'] = user.id
        request.session['member_name'] = user.name
        request.session['member_surname'] = user.surname
        return render(request,"register_panel.html",{'hideLoginPanel' : False, 'successfullRegistration' : True})

    except IntegrityError:
        return render(request,"register_panel.html",{'hideLoginPanel' : True ,'registerError' : "Podany email już istnieje."})
    except:
        return render(request,"register_panel.html",{'hideLoginPanel' : True, 'registerError' : "Coś poszło nie tak spróbuj ponownie."})

