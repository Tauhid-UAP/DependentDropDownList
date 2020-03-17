from django.db import models

# Create your models here.

MALE_CATEGORIES = [

        ('Male Category 1', 'Male Category 1'),
        ('Male Category 2', 'Male Category 2'),

    ]

FEMALE_CATEGORIES = [

        ('Female Category 1', 'Female Category 1'),
        ('Female Category 2', 'Female Category 2'),

    ]

def get_gender_category_choices(gender):

    if gender == 'Male':
        return MALE_CATEGORIES
    elif gender == 'Female':
        return FEMALE_CATEGORIES
    else:
        return []


class Person(models.Model):

    GENDER_CHOICES = [

        ('Male', 'Male'),
        ('Female', 'Female'),

    ]

    # MALE_CATEGORIES = [
    #
    #     ('Male Category 1', 'Male Category 1'),
    #     ('Male Category 2', 'Male Category 2'),
    #
    # ]
    #
    # FEMALE_CATEGORIES = [
    #
    #     ('Female Category 1', 'Female Category 1'),
    #     ('Female Category 2', 'Female Category 2'),
    #
    # ]


    name = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    category = models.CharField(max_length=20, choices=[('', ''), ])