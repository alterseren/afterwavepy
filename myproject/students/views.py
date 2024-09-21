from django.http import HttpResponse
from django.shortcuts import render

def students_home(request):
    return HttpResponse("Головна сторінка студентів")

def student1(request):
    return HttpResponse("Інформація про студента 1")

def student2(request):
    return HttpResponse("Інформація про студента 2")

def student3(request):
    return HttpResponse("Інформація про студента 3")

def student4(request):
    return HttpResponse("Інформація про студента 4")
