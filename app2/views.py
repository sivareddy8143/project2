from django import http
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app(reqest):
    return HttpResponse('this is a second app')
