from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals


def index(request):
    return HttpResponse(ScrumyGoals.objects.filter(goals_name="Learn Django"))

def move_goal(request, goal_id):
    goal = ScrumyGoals.objects.get(goals_id=goal_id)
    return HttpResponse(goal.goals_name)



#Create your views here.
