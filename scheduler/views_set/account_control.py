from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from ..models import SurveyUser


def logout(request):
    try:
        del request.session['member_id']
        del request.session['member_name']
        del request.session['member_surname']
    except KeyError:
        pass
    return render(request,"main.html", {})


def login(request):
    try:
        user = SurveyUser.objects.get(email=request.POST['email'])
    except:
        return render(request,"main.html", {'loginError' : "Nieprawidłowy email"})

    else:
        hashed= make_password(password=request.POST['password'],
                      salt=None,
                      hasher='unsalted_md5')
        if user.hash_of_password == hashed:
            request.session['member_id'] = user.id
            request.session['member_name'] = user.name
            request.session['member_surname'] = user.surname
            return render(request, "main.html", {'logedIn' : True})
        else:
            return render(request, "main.html", {'loginError' : "Nieprawidłowe hasło"})


def isLogedIn(request):
    if 'member_id' in request.session.keys():
        return True
    else:
        return False