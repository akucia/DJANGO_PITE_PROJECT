from django.shortcuts import render
from datetime import datetime

# Create your views here.
def main(request):
    return render(request, 'main.html')


def surveyManager(request):
    d=datetime.now()

    L=[]
    for i in range(0,10,2):

        L.append((i,i+1,d,d.now))

    L.append((10,11,None,None))

    return render(request,"survey_manager_panel.html",{'dateTimes' : L })




# TODO zmien render tak aby odświeżał stronę a nie ładował main.html



