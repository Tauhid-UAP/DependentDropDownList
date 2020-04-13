from django.db import models

# Create your models here.

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

MALE_CATEGORY_1 = 'Male Category 1'
MALE_CATEGORY_2 = 'Male Category 2'
MALE_CATEGORY_3 = 'Male Category 3'

FEMALE_CATEGORY_1 = 'Female Category 1'
FEMALE_CATEGORY_2 = 'Female Category 2'
FEMALE_CATEGORY_3 = 'Female Category 3'

MALE_CATEGORIES = [
    (MALE_CATEGORY_1, MALE_CATEGORY_1),
    (MALE_CATEGORY_2, MALE_CATEGORY_2),
    (MALE_CATEGORY_3, MALE_CATEGORY_3),
]

FEMALE_CATEGORIES = [
    (FEMALE_CATEGORY_1, FEMALE_CATEGORY_1),
    (FEMALE_CATEGORY_2, FEMALE_CATEGORY_2),
    (FEMALE_CATEGORY_3, FEMALE_CATEGORY_3),
]

def get_all_category_choices():
    all_choices = MALE_CATEGORIES
    all_choices+=FEMALE_CATEGORIES

    return all_choices

def get_all_male_category_strings():
    all_male_strings = [
        MALE_CATEGORY_1,
        MALE_CATEGORY_2,
        MALE_CATEGORY_3,
    ]

    return all_male_strings


def get_all_female_category_strings():
    all_female_strings = [
        FEMALE_CATEGORY_1,
        FEMALE_CATEGORY_2,
        FEMALE_CATEGORY_3,
    ]

    return all_female_strings

SUBJECT_CHOICES = [
    ('Computer Science', 'Computer Science'),
    ('Business', 'Business'),
]

CS_1 = 'Software Engineer'
CS_2 = 'Data Scientist'

B_1 = 'Accountant'
B_2 = 'Financial Analyst'

CS_JOBS = [
    (CS_1, CS_1),
    (CS_2, CS_2),
]

BUSINESS_JOBS = [
    (B_1, B_1),
    (B_2, B_2),
]

def get_all_job_choices():
    all_choices = CS_JOBS
    all_choices+=BUSINESS_JOBS

    return all_choices

def get_all_cs_jobs():
    all_cs_strings = [
        CS_1,
        CS_2,
    ]

    return all_cs_strings


def get_all_business_jobs():
    all_business_strings = [
        B_1,
        B_2,
    ]

    return all_business_strings

class Person(models.Model):
    name = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    category = models.CharField(max_length=20, choices=get_all_category_choices())
    # subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    # job = models.CharField(max_length=20, choices=get_all_job_choices())