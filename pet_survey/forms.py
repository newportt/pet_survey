# -*- coding: utf-8 -*-

from django import forms
from django.utils.text import slugify

from pet_survey.models import Pet


class PetForm(forms.ModelForm):
    field_order = ['id', 'owner_name', 'owner_email', 'name']

    def __init__(self, *args, **kwargs):
        super(PetForm, self).__init__(*args, **kwargs)
        field_labels = {
            'name': "Your pet's name is",
            'owner_email': 'Your email address is',
            'owner_name': 'Your name is'
        }
        for field, label in field_labels.items():
            self.fields[field].label = label
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields['id'].required = False
        self.fields['id'].widget = forms.HiddenInput()

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

        return self.cleaned_data

    class Meta:
        model = Pet
        exclude = ['created']
