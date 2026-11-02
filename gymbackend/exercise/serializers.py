from rest_framework import serializers
from .models import ExerciseLog

class ExerciseLogSerializer(serializers.ModelSerializer):
    exercise_display = serializers.CharField(source='get_exercise_display', read_only=True)

    class Meta:
        model = ExerciseLog
        fields = [
            'id',
            'member',
            'exercise',
            'exercise_display',
            'sets',
            'reps',
            'weight',
            'date'
        ]
        read_only_fields = ['id', 'date', 'member', 'exercise_display']

    def create(self, validated_data):
        request = self.context.get('request')
        if not request or not hasattr(request.user, 'gym_profile'):
            raise serializers.ValidationError("No GymMember profile found for this user.")
        
        validated_data['member'] = request.user.gym_profile 
        return super().create(validated_data)
