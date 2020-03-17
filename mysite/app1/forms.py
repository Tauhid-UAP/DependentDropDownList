from django.forms import Form, ModelForm

from .models import Person

class PersonForm(ModelForm):

    class Meta:
        model = Person

        fields = [

            'name',
            'gender',
            'category',

        ]