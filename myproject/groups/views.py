from django.http import HttpResponse
from django.shortcuts import render

def groups_home(request):
    return HttpResponse("Головна сторінка груп")

def group1(request):
    return HttpResponse("Інформація про групу 1")

def group2(request):
    return HttpResponse("Інформація про групу 2")

def group3(request):
    return HttpResponse("Інформація про групу 3")

def group4(request):
    return HttpResponse("Інформація про групу 4")
