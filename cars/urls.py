from django.contrib import admin
from django.urls import path, include
from cars.views import *

app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('all/', CarListView.as_view()),
    path('car/detail/<int:pk>/', CarDeleteView.as_view())
]