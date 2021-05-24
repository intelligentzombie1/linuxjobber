from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.get_grading_parameters, name='kayodescrumy/'),
    path('movegoal/<int:goal_id>/', views.move_goal, name='move_goal')
]