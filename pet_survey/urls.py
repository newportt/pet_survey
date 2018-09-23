# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin

from pet_survey.views import PetSurveyView

urlpatterns = [
    url(r'^$', PetSurveyView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
]
