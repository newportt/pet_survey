# -*- coding: utf-8 -*-

from datetime import date

from django import forms
from django.utils.text import slugify

from pet_survey.models import Pet


class PetForm(forms.ModelForm):
    field_order = ['id', 'owner_name', 'owner_email', 'name', 'gender', 'is_fixed',
                   'birth_month', 'weight', 'breed_count', 'breed_1', 'breed_2']

    def __init__(self, *args, **kwargs):
        super(PetForm, self).__init__(*args, **kwargs)

        # Set the `id` field to be hidden and not required, the value will be populated
        # by the clean() method.
        self.fields['id'].required = False
        self.fields['id'].widget = forms.HiddenInput()

        # Update the available years to select for the `birth_month` widget.
        available_years = [date.today().year - i for i in range(20)]
        self.fields['birth_month'] = forms.DateField(widget=forms.SelectDateWidget(years=available_years))

        # Set the labels for each field, and add Bootstrap's expected CSS class
        field_labels = {
            'birth_month': 'Your pet was born in',
            'breed_count': 'Your pet is a',
            'breed_1': '',
            'breed_2': 'and',
            'gender': 'Your pet is',
            'is_fixed': 'Is your pet spayed/neutered?',
            'name': "Your pet's name is",
            'owner_email': 'Your email address is',
            'owner_name': 'Your name is',
            'weight': "Your pet's weight (in pounds)"
        }
        for field, label in field_labels.items():
            self.fields[field].label = label
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super(PetForm, self).clean()
        if cleaned_data['owner_name'] and cleaned_data['name']:
            # Concatenate the `owner_name` and `name` to generate a unique `id` slug.
            base_slug = slug = slugify(u'{} {}'.format(cleaned_data['owner_name'], cleaned_data['name']))
            is_duplicate_slug = Pet.objects.filter(id=base_slug).exists()
            count = 1
            while is_duplicate_slug:
                slug = '{}-{}'.format(
                    # Truncate the slug depending on the length of `count` as a string and allowing
                    # for the extra '-'.
                    base_slug[:self.fields['id'].max_length - (len(str(count)) + 1)],
                    count
                )
                is_duplicate_slug = Pet.objects.filter(id=slug).exists()
                count += 1

            self.cleaned_data['id'] = slug

        if cleaned_data['breed_count'] == 1 and not cleaned_data['breed_1']:
            self.add_error('breed_1', 'This field is required.')
        elif cleaned_data['breed_count'] == 2:
            if not cleaned_data['breed_1']:
                self.add_error('breed_1', 'This field is required.')

            if not cleaned_data['breed_2']:
                self.add_error('breed_2', 'This field is required.')

        return self.cleaned_data

    class Meta:
        model = Pet
        exclude = ['created']
