from django.shortcuts import render
from datetime import datetime , timedelta
from ..models import *
import string
import random
from dateutil import parser
from django.core.urlresolvers import reverse
from django.utils import timezone
import json
from django.contrib.auth.hashers import make_password


def jq_surveyAnswer(request):
    return render(request, "jq_surveyAnswer.html")

