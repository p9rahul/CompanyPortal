from django.urls import path
from django.urls import re_path as url
from Employee import views


urlpatterns = [
    url(r'^employee$', views.employee),
    url(r'^employee/([0-9]+)$', views.employee)
]