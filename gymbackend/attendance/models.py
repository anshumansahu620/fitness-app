from django.db import models
from account.models import GymMember

STATUS_CHOICES = [
    ('P', 'PRESENT'),
    ('A', 'ABSENT'),
]

class AttendanceModel(models.Model):
    member = models.ForeignKey(
        GymMember, 
        on_delete=models.CASCADE, 
        related_name='attendance_records'
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='P'
    )
    entry_time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendance Records"
        ordering = ['-date', '-entry_time']

    def __str__(self):
        return f"{self.member} - {self.get_status_display()} on {self.date}"
