from django.urls import path
from insurance import views

urlpatterns = [
    path('', views.showtypes, name='showtypes')
]