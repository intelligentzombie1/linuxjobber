from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_grading_parameters, name='blog-home'),
    path('movegoal/<int:goal_id>/', views.move_goal, name='move_goal')
]

