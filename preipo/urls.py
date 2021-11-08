from django.urls import path
from preipo import views

urlpatterns = [
    path('', views.showipo, name='showipo'),
    path('<slug:url>', views.showIpoData, name='showIpoData')
]