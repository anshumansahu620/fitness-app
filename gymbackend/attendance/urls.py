from django.urls import path
from .views import MarkAttendanceView, GetAttendance

urlpatterns = [
    # Mark today's attendance
    path('mark/', MarkAttendanceView.as_view(), name='mark-attendance'),

    # Get attendance for a month
    path('get/', GetAttendance.as_view(), name='get-attendance'),
]

