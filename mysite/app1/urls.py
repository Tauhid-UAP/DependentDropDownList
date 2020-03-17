from django.urls import path
from . import views

# app_name='app1'

urlpatterns = [

    # path('', views.show_all_athletes_page, name='show_all_athletes_page'),
    path('', views.personform_page, name='personform_page'),

]