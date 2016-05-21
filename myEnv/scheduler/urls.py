from django.conf.urls import url
from .views_set.account_control import logout, login
from .views import *
from .views_set.register_control import registerRequest,registerView
from .views_set.survey_manager_control import saveSurvey, surveyManager
from .views_set.survey_answer_control import saveAnswer, surveyAnswer
from .views_set.account_manager import accountManager,removeElement

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

    url(r'^removeElement',removeElement,name="removeElement")
]