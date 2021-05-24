from django.db import models
from django.contrib.auth.models import User

class GoalStatus(models.Model):
    status_name = models.TextField()

    #def __str__(self):
        #return self.status_name


class ScrumyGoals(models.Model):
    goal_name = models.TextField()
    goal_id = models.IntegerField()
    created_by = models.TextField()
    moved_by = models.TextField()
    owner = models.TextField()
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT)

    #def __str__(self):
        #return self.goal_name


class ScrumyHistory(models.Model):
    created_by = models.TextField()
    moved_by = models.TextField()
    moved_from = models.TextField()
    moved_to = models.TextField()
    time_of_action = models.TextField()
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.PROTECT)

    #def __str__(self):
        #return self.created_by
