from django import forms
from django.forms import Form, ModelForm

from .models import Person
from .models import GENDER_CHOICES, MALE_CATEGORIES, FEMALE_CATEGORIES
from .models import get_all_choices

class PersonForm(ModelForm):

    class Meta:
        model = Person

        fields = [

            'name',
            'gender',
            'category',

        ]

    # Tried to solve it by cleaning category field
    # def clean_category(self):
    #     category = self.cleaned_data.get('category')
    #
    #     if (category not in MALE_CATEGORIES) & (category not in FEMALE_CATEGORIES):
    #         raise forms.ValidationError(
    #             _('Invalid choice. Please select a valid choice.'),
    #             code='invalid choice',
    #             params=None
    #         )
    #
    #     return category