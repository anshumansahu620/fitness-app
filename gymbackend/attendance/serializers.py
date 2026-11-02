from rest_framework import serializers
from .models import AttendanceModel

class AttendanceSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source='member.name', read_only=True)  # assuming GymMember has `name`
    
    class Meta:
        model = AttendanceModel
        fields = [
            'id',
            'member',
            'member_name',
            'status',
            'entry_time',
            'date',
        ]
        read_only_fields = ['entry_time', 'date']



class AttendanceDateSerializers(serializers.ModelSerializer):
    class Meta:
        model=AttendanceModel
        fields=['status','date']
        