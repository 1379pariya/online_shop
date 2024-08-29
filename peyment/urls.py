from django.urls import path
from . import views

urlpatterns = [
    path('', views.peyment_list, name = 'peyment_list')
]