from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse(".")

def login(request):
    return HttpResponse("!!")