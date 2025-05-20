from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello Django!", content_type="text/plain")
# Create your views here.
