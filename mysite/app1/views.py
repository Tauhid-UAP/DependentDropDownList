from django.shortcuts import render, redirect

from .models import Person
from .forms import PersonForm

from .models import GENDER_CHOICES, MALE_CATEGORIES, FEMALE_CATEGORIES

# Create your views here.

def personform_page(request):

    context = {}

    if request.method == 'POST':
        personform = PersonForm(request.POST)

        if personform.is_valid():
            personform.save()
            return redirect('personform_page')

        context['personform'] = personform

    else:
        personform = PersonForm()
        context['personform'] = personform

    context['male_categories'] = MALE_CATEGORIES
    context['female_categories'] = FEMALE_CATEGORIES

    return render(request, 'app1/personform_page.html', context=context)