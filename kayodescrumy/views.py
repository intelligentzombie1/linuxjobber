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


def add_goal(request):
    ScrumyGoals.objects.create(
        user=User.objects.get(username='LouisOma'),
        goal_name='Keep Learning Django',
        goal_id= random.randint(1000,9999),
        created_by = 'Louis',
        moved_by='Louis',
        owner='Louis',
        goal_status=GoalStatus.objects.get(status_name='Weekly Goal')
    )


def home(request):
   # display = ScrumyGoals.objects.get(goal_name='Keep Learning Django')
    #output = ', '.join([q.goal_name for q in display])
    goal_name = ScrumyGoals.objects.get(goal_name='Learn Django')
    goal_id = (ScrumyGoals.objects.get(goal_id=1))
    user = User.objects.get(username='louis')
    context = {
        'goal_name': goal_name,
        'goal_id': goal_id,
        'user': user,
    }
    return render(request, 'kayodescrumy/home.html', context)