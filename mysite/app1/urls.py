from django.urls import path
from . import views

# app_name='app1'

urlpatterns = [
    # path('', views.show_all_athletes_page, name='show_all_athletes_page'),
    path('personform_page/', views.personform_page, name='personform_page'),
    path('show_all_persons_page/', views.show_all_persons_page, name='show_all_persons_page'),
]