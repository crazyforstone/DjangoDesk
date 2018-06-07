from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

# Create your views here.

def index(request):
    return HttpResponse('hello world')