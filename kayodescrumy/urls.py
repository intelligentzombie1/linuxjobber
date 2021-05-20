from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-home'),
    path("move_goal/<int:goal_id>", views.move_goal),
]
