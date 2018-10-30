from django.urls import path

from . import views

urlpatterns = [
    path('', views.input, name='input'),
    path('results/', views.results, name='results'),
]