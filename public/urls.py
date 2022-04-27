from django.urls import path

from public import views

urlpatterns = [
    path('', views.index, name='index'),
]