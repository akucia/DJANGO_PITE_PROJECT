from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'main.html')


def surveyManager(request):
    return render(request,"survey_manager_panel.html")




# TODO zmien render tak aby odświeżał stronę a nie ładował main.html



