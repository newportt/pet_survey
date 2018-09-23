# -*- coding: utf-8 -*-

from django.contrib import admin

from pet_survey.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
