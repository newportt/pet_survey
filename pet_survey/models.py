# -*- coding: utf-8 -*-

from django.db import models


class Pet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.SlugField(max_length=126, primary_key=True)
    name = models.CharField(max_length=25)
    owner_email = models.EmailField()
    owner_name = models.CharField(max_length=100)
