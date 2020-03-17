from django.shortcuts import render

from .models import Person
from .forms import PersonForm

# Create your views here.

def personform_page(request):

    context = {}

    personform = PersonForm()

    context['personform'] = personform

    return render(request, 'app1/personform_page.html', context)