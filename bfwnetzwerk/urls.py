from django.urls import path

from . import views

urlpatterns = [
    path('form1', views.form1, name='index'),
]