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

