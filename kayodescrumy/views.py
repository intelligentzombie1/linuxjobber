from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals


def get_grading_parameters(request):
    return HttpResponse(ScrumyGoals.objects.filter(goal_name='Learn Django'))




#Create your views here.
