# -*- coding: utf-8 -*-

from django.urls import reverse
from django.views.generic import FormView

from pet_survey.forms import PetForm


class PetSurveyView(FormView):
    form_class = PetForm
    template_name = 'pet_survey_form.html'

    def form_valid(self, form):
        self.object = form.save()
        return super(PetSurveyView, self).form_valid(form)

    def get_success_url(self):
        return reverse('index')
