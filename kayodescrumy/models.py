from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class GoalStatus(models.Model):
    status_name = models.CharField(max_length=300)



class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length=300)
    goal_id = models.IntegerField()
    created_by = models.CharField(max_length=300)
    moved_by = models.CharField(max_length=300)
    owner = models.CharField(max_length=300)
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT)


class ScrumyHistory(models.Model):
    created_by = models.CharField(max_length=300)
    moved_by = models.CharField(max_length=300)
    moved_from = models.CharField(max_length=300)
    moved_to = models.CharField(max_length=300)
    time_of_action = models.TimeField()
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.PROTECT)
