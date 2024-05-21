from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'doctorprofile'

urlpatterns=[
    path('', views.doctor_profile, name='doctor-page'),
    path('forms/', views.forms , name='forms'),
    path('forms/<str:status>', views.forms , name='forms'),
    path('editinfo/', views.edit_info, name='edit-info'),
    # path('respond/', views.respond, name = 'respond'),

    path('test/', views.test),
]