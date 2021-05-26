from django.shortcuts import render
import random
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import ScrumyGoals, GoalStatus


# Create your views here.
def get_grading_parameters(request):
    return HttpResponse(ScrumyGoals.objects.filter(goal_name='Learn Django'))


def move_goal(request, goal_id):
    goal = ScrumyGoals.objects.get(goal_id=goal_id)
    return HttpResponse(goal.goal_name)


def add_goal(request, ):
    users = User.objects.get(username='LouisOma')
    goal_status = GoalStatus.objects.get(status_name='Weekly Goal')
    ids = random.randint(1000, 9999)
    ScrumyGoals.objects.create(goal_name='Keep Learning Django', goal_id=ids,
                               created_by='Louis', moved_by='Louis', owner='Louis',
                               goal_status=goal_status, user=users),


def home(request,):
    display = ScrumyGoals.objects.filter(goal_name='Keep Learning Django')
    output = ', '.join([eachgoal.goal_name for eachgoal in display])
    return HttpResponse(output)
