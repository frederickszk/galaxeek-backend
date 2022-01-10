from django.urls import path
from api import views

urlpatterns = [
    path('position_list', views.position_list)
]