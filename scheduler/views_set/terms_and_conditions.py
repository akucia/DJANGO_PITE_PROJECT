from django.shortcuts import render


def termsAndConditions(request):
    return render(request, 'terns_and_conditions_template.html', {} )