from django.shortcuts import render
from ..models import *


def toastr_test(request):
   return render(request,"toastr_test.html")
