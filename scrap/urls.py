from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.data_input, name='data_input'),
    path('with_attributes', views.with_attributes, name='with_attributes'),
]
