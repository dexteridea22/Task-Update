from django.urls import path
from .views import ListTasksView



urlpatterns = [
    path('tasks/', ListTasksView.as_view(), name="tasks-all")
]