from django.shortcuts import render
from django.core import serializers
from .models import Shop
import environ
# Declring environ
env = environ.Env()
# Read env file
environ.Env.read_env()

# Create your views here.


def near_shops(request):
    shops = serializers.serialize("json", Shop.objects.all())
    context = {"google_api_key":  env('GOOGLE_MAPS_API_KEY'),
               "shops": shops}
    return render(request, 'home_page.html', context)
