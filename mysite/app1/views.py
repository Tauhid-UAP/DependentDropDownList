from django.shortcuts import render, redirect
from django.core.paginator import Paginator
import json

from .models import Person
from .forms import PersonForm

from .models import get_all_male_category_strings, get_all_female_category_strings
from .models import get_all_cs_jobs, get_all_business_jobs

from .filters import PersonFilter

from .models import GENDER_CHOICES, MALE_CATEGORIES, FEMALE_CATEGORIES
from .models import SUBJECT_CHOICES, CS_JOBS, BUSINESS_JOBS

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

    male_category_list = get_all_male_category_strings()
    female_category_list = get_all_female_category_strings()

    # cs_job_list = get_all_cs_jobs()
    # business_job_list = get_all_business_jobs()

    json_male_categories = json.dumps(male_category_list)
    json_female_categories = json.dumps(female_category_list)

    # json_cs_jobs = json.dumps(cs_job_list)
    # json_business_jobs = json.dumps(business_job_list)

    context['json_male_categories'] = json_male_categories
    context['json_female_categories'] = json_female_categories

    # context['json_cs_jobs'] = json_cs_jobs
    # context['json_business_jobs'] = json_business_jobs

    return render(request, 'app1/personform_page.html', context=context)

# def personform_page(request):
#
#     context = {}
#
#     if request.method == 'POST':
#         personform = PersonForm(request.POST)
#
#         if personform.is_valid():
#             personform.save()
#             return redirect('personform_page')
#
#         context['personform'] = personform
#
#     else:
#         personform = PersonForm()
#         context['personform'] = personform
#
#     # male_category_list = get_all_male_category_strings()
#     # female_category_list = get_all_female_category_strings()
#
#     cs_job_list = get_all_cs_jobs()
#     business_job_list = get_all_business_jobs()
#
#     # json_male_categories = json.dumps(male_category_list)
#     # json_female_categories = json.dumps(female_category_list)
#
#     json_cs_jobs = json.dumps(cs_job_list)
#     json_business_jobs = json.dumps(business_job_list)
#
#     # context['json_male_categories'] = json_male_categories
#     # context['json_female_categories'] = json_female_categories
#
#     context['json_cs_jobs'] = json_cs_jobs
#     context['json_business_jobs'] = json_business_jobs
#
#     return render(request, 'app1/personform_page1.html', context=context)

def show_all_persons_page(request):
    context = {}

    filtered_person_list = PersonFilter(
        request.GET,
        queryset=Person.objects.all()
    )

    context['filtered_person_list'] = filtered_person_list

    paginated_filtered_person_list = Paginator(filtered_person_list.qs, 3)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filtered_person_list.get_page(page_number)

    context['person_page_obj'] = person_page_obj

    return render(request, 'app1/show_all_persons_page.html', context)

# def show_all_persons_page(request):
#     context = {}
#     person_list = Person.objects.all()
#
#     # Filter the list based on the criteria
#     # If the filter button is pressed
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         gender = request.POST.get('gender')
#         category = request.POST.get('category')
#
#         if name != "":
#             person_list = [person for person in person_list if person.name == name]
#         if gender != "":
#             person_list = [person for person in person_list if person.gender == gender]
#         if category != "":
#             person_list = [person for person in person_list if person.category == category]
#
#     # GET
#     male_category_list = get_all_male_category_strings()
#     female_category_list = get_all_female_category_strings()
#
#     json_male_categories = json.dumps(male_category_list)
#     json_female_categories = json.dumps(female_category_list)
#
#     context['json_male_categories'] = json_male_categories
#     context['json_female_categories'] = json_female_categories
#
#     paginated_person_list = Paginator(person_list, 4)
#     page_number = request.GET.get('page')
#     person_page_obj = paginated_person_list.get_page(page_number)
#
#     context['person_page_obj'] = person_page_obj
#
#     return render(request, 'app1/show_all_persons_page.html', context)