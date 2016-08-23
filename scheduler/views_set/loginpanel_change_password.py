from django.shortcuts import render
from datetime import datetime, timedelta
from ..models import *
import string
import random
from dateutil import parser
from django.core.urlresolvers import reverse
from django.utils import timezone
import json
import random

from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

def changePassword(request):
	if 'code' in request.POST:
		return changePasswordFinal(request)
	if 'email' in request.POST:
		try:
			user = SurveyUser.objects.get(email=request.POST['email'])
		except:
			error_token="Podany email nie został odnaleziony."
			change_panel=False
			return render(request, "change_password.html",locals())
			
		code=""
		while len(code) != 6 :
			i=random.randint(48, 90)
			while i > 57 and i < 65:
				i=random.randint(48, 90)
			code=code+chr(i)
			
		
		email=request.POST['email']
		try:
			send_mail(
    			'PITE zmiana hasła',
    			'Prosiłeś o zmianę hasła. Wygenerowany kod to :'+code,
    			'admin@pite.pl',
    			email,
    			fail_silently=False,
				)
		except:
			pass
			
		success_token="Na podanego emaila został wysłany kod. Nie zamykaj tej strony."
		code="123456"
		change_panel=True
		code= make_password(password=code,salt=None,hasher='unsalted_md5')
		return render(request, "change_password.html",locals())
	change_panel=False
	return render(request, "change_password.html",locals())
	
	
def changePasswordFinal(request):
	code=make_password(password=request.POST['code'],salt=None,hasher='unsalted_md5')
	if request.POST['s_code'] != code :
		code=request.POST['s_code']
		email=request.POST['email']
		change_panel=True
		error_token="Podano niewłaściwy kod"
		return render(request, "change_password.html",locals())
	else:
		if request.POST['pass'] != request.POST['rpass'] :
			code=request.POST['s_code']
			email=request.POST['email']
			change_panel=True
			error_token="Podane hasła nie są zgodne"
			return render(request, "change_password.html",locals())
		else:
			user = SurveyUser.objects.get(email=request.POST['email'])
			user.hash_of_password=make_password(request.POST['pass'],salt=None,hasher='unsalted_md5')
			user.save()
			change_panel=False
			success_token="Hasło zostało zmienione pomyślnie"
			return render(request, "change_password.html",locals())
