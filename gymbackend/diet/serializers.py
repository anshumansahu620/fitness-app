from rest_framework import serializers
from .models import DietEntry

class DietEntrySerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source='member.name', read_only=True)

    class Meta:
        model = DietEntry
        fields = [
            'id',
            'member',
            'member_name',
            'meal_name',
            'food_data',
            'total_calories',
            'total_protein',
            'total_carbs',
            'total_fats',
            'date',
            'created_at'
        ]
        read_only_fields = ['date', 'created_at']
    def create(self, validated_data):
        request = self.context.get('request')
        if not request or not hasattr(request.user, 'gym_profile'):
            raise serializers.ValidationError("No GymMember profile found for this user.")
        
        validated_data['member'] = request.user.gym_profile 
        return super().create(validated_data)
