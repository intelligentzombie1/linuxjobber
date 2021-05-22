from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-home'),
    path("movegoal/<int:goal_id>", views.move_goal),
]
