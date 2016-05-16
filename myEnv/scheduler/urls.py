from django.conf.urls import url
from .views_set.account_control import logout, login
from .views import *
from .views_set.register_control import registerRequest,registerView
urlpatterns = [
    url(r'^$', main, name='main_view'),
    url(r'^logOut$', logout, name='logOut'),
    url(r'^logIn$', login, name='logIn'),
    url(r'^registerView$', registerView, name='registerView'),
    url(r'^registerRequest$', registerRequest, name='registerRequest'),
    url(r'^surveyManager', surveyManager, name='surveyManager'),

    url(r'^saveSurvey',main,name="saveSurvey")
]