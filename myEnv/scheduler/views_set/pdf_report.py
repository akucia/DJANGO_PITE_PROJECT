from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from subprocess import Popen, PIPE
import os
import tempfile
from django.shortcuts import render
from ..models import *


def pdfReport(request):

    row=None
    if 'adminID' in request.GET.keys():
        adminID=request.GET['adminID']
        try:
            row=Survey.objects.get(adminID=request.GET['adminID'])
        except:
            return render(request,"some_error_panel.html",{ 'errorDescription' : "Podany przez Ciebie numer ID nie występuje w bazie ankiet" })

        listOfAnswers=[]
        answers=Answer.objects.filter(survey=row)

        for fromDate,toDate in row.fields:
            listOfMatches=[]
            for answer in answers:
                try:
                    if answer.answer[(fromDate,toDate)]:
                        listOfMatches.append((answer.name,answer.surname,answer.email))
                except:
                    pass
            listOfAnswers.append((fromDate,toDate,listOfMatches))

        context = Context({'answerDates': listOfAnswers,
                           'title' : row.title ,
                           'description' : row.description,
                           'creationDate' : row.creation_date
        })
        template = get_template('report_template.tex')
        rendered_tpl = template.render(context).encode('utf-8')
        # Python3 only. For python2 check out the docs!
        with tempfile.TemporaryDirectory() as tempdir:
            # Create subprocess, supress output with PIPE and
            # run latex twice to generate the TOC properly.
            # Finally read the generated pdf.
            for i in range(2):
                process = Popen(
                    ['pdflatex', '-output-directory', tempdir],
                    stdin=PIPE,
                    stdout=PIPE,
                )
                process.communicate(rendered_tpl)
            with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:
                pdf = f.read()
        r = HttpResponse(content_type='application/pdf')
        # r['Content-Disposition'] = 'attachment; filename=texput.pdf'
        r.write(pdf)
        return r
    else:
        return render(request,"some_error_panel.html",{ 'errorDescription' : "Nie działa"})

