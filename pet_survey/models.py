# -*- coding: utf-8 -*-

from django.db import models


class Pet(models.Model):
    BREED_COUNT_CHOICES = (
        (0, 'Breed not known'),
        (1, 'One primary breed'),
        (2, 'Two primary breeds'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    birth_month = models.DateField()
    breed_count = models.IntegerField(choices=BREED_COUNT_CHOICES)
    breed_1 = models.ForeignKey('pet_survey.Breed', null=True, blank=True, related_name='+')
    breed_2 = models.ForeignKey('pet_survey.Breed', null=True, blank=True, related_name='+')
    created = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    id = models.SlugField(max_length=126, primary_key=True)
    is_fixed = models.BooleanField()
    name = models.CharField(max_length=25)
    owner_email = models.EmailField()
    owner_name = models.CharField(max_length=100)
    weight = models.PositiveIntegerField()

    def __unicode__(self):
        return u'{} - {}'.format(self.owner_name, self.name)


class Breed(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
