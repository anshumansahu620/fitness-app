from django.db import models
from account.models import GymMember

class DietEntry(models.Model):
    member = models.ForeignKey(
        GymMember,
        on_delete=models.CASCADE,
        related_name='diet_entries'
    )
    meal_name = models.CharField(max_length=50)  # e.g. Breakfast, Lunch, Dinner, Snack
    food_data = models.JSONField()  # frontend sends JSON with all nutrition info
    total_calories = models.FloatField(default=0)
    total_protein = models.FloatField(default=0)
    total_carbs = models.FloatField(default=0)
    total_fats = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.member} - {self.meal_name} ({self.date})"
