from django.shortcuts import render, redirect
from django.core.paginator import Paginator

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

def show_all_persons_page(request):
    context = {}
    person_list = Person.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        category = request.POST.get('category')

        if name is not "":
            person_list = [person for person in person_list if person.name == name]
        if gender is not "":
            person_list = [person for person in person_list if person.gender == gender]
        if category is not "":
            person_list = [person for person in person_list if person.category == category]

    context['person_list'] = person_list

    paginated_person_list = Paginator(person_list, 4)
    page_number = request.GET.get('page')
    person_page_obj = paginated_person_list.get_page(page_number)

    context['person_page_obj'] = person_page_obj

    return render(request, 'app1/show_all_persons_page.html', context)