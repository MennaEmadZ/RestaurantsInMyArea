from django.urls import path
from . import views

urlpatterns = [
    path('', views.near_shops, name="shops"),
]
