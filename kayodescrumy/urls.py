from django.urls import include, path
from . import views

app_name = "kayodescrumy"

urlpatterns = [
    path('', views.get_grading_parameters, name='about/'),
    path('movegoal/<int:goal_id>/', views.move_goal, name='move_goal'),
    path('addgoal/', views.add_goal, name='addgoal'),
    path('home/', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls'))
]