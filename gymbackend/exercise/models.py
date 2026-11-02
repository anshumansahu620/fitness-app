from django.db import models
from account.models import GymMember 


EXERCISES = [
    ("Push Ups", "Push Ups"),
    ("Bench Press", "Bench Press"),
    ("Incline Dumbbell Press", "Incline Dumbbell Press"),
    ("Chest Fly", "Chest Fly"),
    ("Squats", "Squats"),
    ("Lunges", "Lunges"),
    ("Leg Press", "Leg Press"),
    ("Leg Extension", "Leg Extension"),
    ("Pull Ups", "Pull Ups"),
    ("Lat Pulldown", "Lat Pulldown"),
    ("Barbell Row", "Barbell Row"),
    ("Deadlift", "Deadlift"),
    ("Bicep Curls", "Bicep Curls"),
    ("Hammer Curls", "Hammer Curls"),
    ("Tricep Dips", "Tricep Dips"),
    ("Tricep Pushdown", "Tricep Pushdown"),
    ("Plank", "Plank"),
    ("Crunches", "Crunches"),
    ("Russian Twists", "Russian Twists"),
    ("Mountain Climbers", "Mountain Climbers"),
    ("Treadmill Run", "Treadmill Run"),
    ("Cycling", "Cycling"),
    ("Jump Rope", "Jump Rope"),
    ("Burpees", "Burpees"),
]

# 🔹 Exercise Log Model
class ExerciseLog(models.Model):
    member = models.ForeignKey(
        GymMember,
        on_delete=models.CASCADE,
        related_name="exercise_logs"
    )
    exercise = models.CharField(max_length=100, choices=EXERCISES)
    sets = models.PositiveIntegerField(default=3)
    reps = models.PositiveIntegerField(default=10)
    weight = models.FloatField(default=0.0, help_text="Weight used in kg (optional)")
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Exercise Log"
        verbose_name_plural = "Exercise Logs"

    def __str__(self):
        return f"{self.member.full_name} - {self.exercise} ({self.sets}x{self.reps}) on {self.date}"
