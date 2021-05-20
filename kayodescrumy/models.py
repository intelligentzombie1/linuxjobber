from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class GoalStatus(models.Model):
    status_name = models.TextField()

    def __str__(self):
        return self.status_name


class ScrumyGoals(models.Model):
    goals_name = models.TextField()
    goals_id = models.IntegerField()
    goals_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    created_by = models.TextField()
    moved_by = models.TextField()
    owner = models.TextField()
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT)

    def __str__(self):
        return self.goals_name

class ScrumyHistory(models.Model):
    created_by = models.TextField()
    moved_by = models.TextField()
    moved_from = models.TextField()
    moved_to = models.TextField()
    time_to_action = models.DateTimeField(default=timezone.now)
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.PROTECT)
