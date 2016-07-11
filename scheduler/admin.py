from django.contrib import admin
from .models import Survey
from .models import SurveyUser
from .models import Answer

admin.site.register(Survey)
admin.site.register(SurveyUser)
admin.site.register(Answer)

# Register your models here.
