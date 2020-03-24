from django.db import models

# Create your models here.

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

MALE_CATEGORIES = [
    ('Male Category 1', 'Male Category 1'),
    ('Male Category 2', 'Male Category 2'),
    ('Male Category 3', 'Male Category 3'),
]

FEMALE_CATEGORIES = [
    ('Female Category 1', 'Female Category 1'),
    ('Female Category 2', 'Female Category 2'),
    ('Female Category 3', 'Female Category 3'),
]

def get_all_choices():
    all_choices = MALE_CATEGORIES
    all_choices+=FEMALE_CATEGORIES

    return all_choices

class Person(models.Model):
    name = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    category = models.CharField(max_length=20, choices=get_all_choices())