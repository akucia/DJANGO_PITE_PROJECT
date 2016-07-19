from django.conf.urls import url
from .views_set.account_control import logout, login
from .views import *
from .views_set.register_control import registerRequest,registerView
from .views_set.survey_manager_control import saveSurvey, surveyManager
from .views_set.survey_answer_control import saveAnswer, surveyAnswer
from .views_set.account_manager import accountManager,removeElement
from .views_set.pdf_report import pdfReport
from .views_set.csv_report import csvReport
from .views_set.html_report import htmlReport
from .views_set.website_stat_control import websiteStatManager
from .views_set.contact_control import contactManager,sendMail
from .views_set.terms_and_conditions import termsAndConditions

urlpatterns = [
    url(r'^$', main, name='main_view'),
    url(r'^logOut$', logout, name='logOut'),
    url(r'^logIn$', login, name='logIn'),
    url(r'^registerView$', registerView, name='registerView'),
    url(r'^registerRequest$', registerRequest, name='registerRequest'),
    url(r'^surveyManager', surveyManager, name='surveyManager'),

    url(r'^saveSurvey',saveSurvey,name="saveSurvey"),
    url(r'^surveyAnswer',surveyAnswer,name="surveyAnswer"),
    url(r'^saveAnswer',saveAnswer,name="saveAnswer"),
    url(r'^accountManager',accountManager,name="accountManager"),
    url(r'^removeElement',removeElement,name="removeElement"),

    url(r"^csv_report",csvReport,name="csvReport"),
    url(r'^pdf_report', pdfReport, name='pdfReport'),
    url(r'^html_report', htmlReport, name='htmlReport'),

    url(r'^websiteStatManager',websiteStatManager,name="websiteStatManager"),
    url(r'^contactManager',contactManager,name="contactManager"),
    url(r'^sendMail',sendMail,name="sendMail"),

    url(r'^termsAndConditions',termsAndConditions,name="termsAndConditions"),

]