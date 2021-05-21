from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals


def index(request):
    return HttpResponse(ScrumyGoals.objects.filter(goal_name="Learn Django"))

def move_goal(request, goal_id):
    goal = ScrumyGoals.objects.get(goal_id=goal_id)
    return HttpResponse(goal.goal_name)



#Create your views here.
