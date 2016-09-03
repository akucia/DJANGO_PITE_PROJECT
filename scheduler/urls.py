from django.conf.urls import url
from .views_set.account_control import logout, login
from .views import *
from .views_set.register_control import registerRequest,registerView
from .views_set.survey_manager_control import saveSurvey, surveyManager
from .views_set.survey_answer_control import saveAnswer, surveyAnswer
from .views_set.account_manager import *
from .views_set.pdf_report import pdfReport
from .views_set.csv_report import csvReport
from .views_set.html_report import htmlReport
from .views_set.website_stat_control import websiteStatManager
from .views_set.contact_control import contactManager,sendMail
from .views_set.terms_and_conditions import termsAndConditions
from .views_set.jq_register_panel import registerAjaxRequest
from .views_set.jq_login_elements import logoutRequestAjax, loginRequestAjax
from .views_set.jq_global_statistic import jqGlobalStatistic
from .views_set.jq_contact import jqContactForm, jqContactSentMailRequest
from  .views_set.jq_restore_password import jqRestorePassword, jqSentRestoreEmailRequest, jqSentNewPasswordRequest
from .views_set.jq_account_management import jqAccountManagement, jqAccountChangeUserdataRequest, jqAccountChangeUserPasswordRequest, jqAccountRemoveSurveyRequest
from .views_set.jq_surveyAnswer import jq_surveyAnswer, jqSurveyAnswerCheckUserIdRequest, jq_SurveyAnswerForm, jq_SurveyAnswerRedirector

from .views_set.toastr_test import toastr_test

from .views_set.loginpanel_change_password import changePassword
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
    url(r'^removeElement',removeElement,name="removeElement"),

    url(r"^csv_report",csvReport,name="csvReport"),
    url(r'^pdf_report', pdfReport, name='pdfReport'),
    url(r'^html_report', htmlReport, name='htmlReport'),
    url(r'^toastr_test', toastr_test, name='toastr_test'),

    url(r'^websiteStatManager',websiteStatManager,name="websiteStatManager"),
    url(r'^contactManager',contactManager,name="contactManager"),
    url(r'^sendMail',sendMail,name="sendMail"),
    url(r'^changePassword',changePassword,name="changePassword"),

    #url for account manager menu
    url(r'^am_userInfo',accountManager_userInfo,name="am_userInfo"),
    url(r'^am_changeUserdata',accountManager_changeUserdata,name="am_changeUserdata"),
    url(r'^am_changeUserpassword',accountManager_changeUserpassword,name="am_changeUserpassword"),
    url(r'^am_userSurveys',accountManager_userSurveys,name="am_userSurveys"),
    url(r'^am_userActivity',accountManager_userActivity,name="am_userActivity"),
    url(r'^sendMail',sendMail,name="sendMail"),

    url(r'^termsAndConditions',termsAndConditions,name="termsAndConditions"),

    # jqery page version
    url(r'^jqStart$',jqMain, name="jq_main"),
    url(r'^hidden/jqNavBar$',jqNavBar, name="jq_navBar"),
    url(r'^hidden/jqDefault$',jqDefault,name="jq_default"),
    url(r'^hidden/jqLoginPane$',jqLoginPane,name="jq_loginPane"),
    url(r'^hidden/jqRegisterPanel$',jqRegisterPanel,name="jq_registerPanel"),
    url(r'^hidden/jqRegisterPanel/registerRequest$',registerAjaxRequest,name="jq_registerPanel_registerRequest"),
    url(r'^hidden/jqLoginElements/logoutRequest$',logoutRequestAjax,name="jq_loginElements_logoutRequest"),
    url(r'^hidden/jqTermsAndConditions$',jqTermsAndConditions,name="jq_termsAndConditions"),
    url(r'^hidden/jqGlobalStatistic$',jqGlobalStatistic, name="jq_globalStatistic"),
    url(r'^hidden/jqLoginElements/loginRequest$', loginRequestAjax, name="jq_loginElements_loginRequest"),
    url(r'^hidden/jqContactForm$',jqContactForm,name="jq_contactForm"),
    url(r'^hidden/jqContactForm/contactSentMailRequest$', jqContactSentMailRequest, name="jq_contact_sentMailRequest"),
    url(r'^hidden/jqRestorePassword$',jqRestorePassword,name="jq_restorePassword"),
    url(r'^hidden/jqRestorePassword/sentRestoreEmailRequest$',jqSentRestoreEmailRequest, name="jq_restorePassword_sentRestoreEmailRequest"),
    url(r'^hidden/jqRestorePassword/sentNewPasswordRequest$',jqSentNewPasswordRequest,name="jq_restorePassword_sentNewPasswordRequest"),
    url(r'^hidden/jqAccountManagement$',jqAccountManagement,name="jq_accountManagement"),
    url(r'^hidden/jqAccountManagement/sentChangeUserdataRequest$',jqAccountChangeUserdataRequest, name="jq_accountManagement_changeUserData"),
    url(r'^hidden/jqAccountManagement/sentChangeUserPasswordRequest$', jqAccountChangeUserPasswordRequest,name="jq_accountManagement_changeUserPassword"),
    url(r'^hidden/jqAccountManagement/sentRemoveSurveyRequest$', jqAccountRemoveSurveyRequest,name="jq_accountManagement_removeSurvey"),
    url(r'^hidden/jqSurveyAnswer$',jq_surveyAnswer,name="jq_surveyAnswer"),
    url(r'^hidden/jqSurveyAnswer/checkIfUserIdIsCorrect$',jqSurveyAnswerCheckUserIdRequest,name="jq_surveyAnswer_checkUserId"),
    url(r'^jqSurveyAnswerForm',jq_SurveyAnswerRedirector,name="surveyAnswerFormRedirector"),
    url(r'^hidden/jqSurveyAnswerForm',jq_SurveyAnswerForm, name="surveyAnswerForm")

]