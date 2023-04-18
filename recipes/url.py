from django.http import HttpResponse
from django.urls import path
from recipes.views import home, contato, sobre

urlpatterns = [
    path('contato/', contato),
    path('sobre/', sobre),
    path('', home)
]