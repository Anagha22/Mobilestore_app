from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Mobile
# Create your views here.
class IndexView(ListView):

    model = Mobile

