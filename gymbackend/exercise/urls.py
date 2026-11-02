# exercise/urls.py
from django.urls import path
from .views import ExerciseLogCreateView, ExerciseLogDeleteView, ExerciseLogListView

urlpatterns = [
    path("", ExerciseLogListView.as_view(), name="exercise-log-list"),        # GET logs
    path("add/", ExerciseLogCreateView.as_view(), name="exercise-log-create"), # POST new log
    path("<int:log_id>/", ExerciseLogDeleteView.as_view(), name="exercise-log-delete"), # DELETE
]
