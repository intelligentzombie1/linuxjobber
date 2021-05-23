from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals


def get_grading_parameters(request):
    return HttpResponse("This is a Scrum Application")




#Create your views here.
