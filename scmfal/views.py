from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'scmfal/home.html')

def course(request):
    return render(request,'scmfal/courses.html')