# account/models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date

class GymMember(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='gym_profile')
    full_name=models.CharField(max_length=255,default='temporary user')
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    phone = models.CharField(max_length=15, unique=True)
    membership_duration = models.CharField(
        max_length=20,
        choices=[
            ('1M', '1 Month'),
            ('3M', '3 Months'),
            ('6M', '6 Months'),
            ('1Y', '1 Year'),
        ],
        default='1M'
    )
    join_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')

    def save(self, *args, **kwargs):
        # Use join_date if exists, else today
        join_date = self.join_date or date.today()
        duration_map = {
            '1M': 30,
            '3M': 90,
            '6M': 180,
            '1Y': 365
        }
        self.expiry_date = join_date + timedelta(days=duration_map.get(self.membership_duration, 30))
        super().save(*args, **kwargs)
