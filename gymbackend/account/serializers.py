# gym/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import GymMember
from datetime import timedelta

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class GymMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = GymMember
        fields = [
            'user',
            'full_name',
            'age',
            'sex',
            'phone',
            'membership_duration',
            'join_date',
            'expiry_date',
            'profile_picture'
        ]


from rest_framework import serializers
from django.contrib.auth.models import User
from .models import GymMember

class RegisterSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(write_only=True)
    age = serializers.IntegerField(write_only=True)
    sex = serializers.ChoiceField(choices=GymMember.SEX_CHOICES, write_only=True)
    phone = serializers.CharField(write_only=True)
    membership_duration = serializers.ChoiceField(
        choices=GymMember._meta.get_field('membership_duration').choices,
        write_only=True
    )
    profile_picture = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            "username", "email", "password",
            "full_name", "age", "sex", "phone",
            "membership_duration", "profile_picture"
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        full_name = validated_data.pop("full_name")
        age = validated_data.pop("age")
        sex = validated_data.pop("sex")
        phone = validated_data.pop("phone")
        membership_duration = validated_data.pop("membership_duration")
        profile_picture = validated_data.pop("profile_picture", None)

        user = User.objects.create_user(**validated_data)

        # Ensure profile_picture is set correctly
        if profile_picture:
            GymMember.objects.create(
                user=user,
                full_name=full_name,
                age=age,
                sex=sex,
                phone=phone,
                membership_duration=membership_duration,
                profile_picture=profile_picture,
            )
        else:
            GymMember.objects.create(
                user=user,
                full_name=full_name,
                age=age,
                sex=sex,
                phone=phone,
                membership_duration=membership_duration,
            )

        return user



class ExtendDurationSerilizer(serializers.Serializer):
    id=serializers.IntegerField()
    extension_days=serializers.IntegerField()


    def create(self,validated_data):
        id=validated_data.get('id')
        extension=validated_data.get('extension_days')

        try:
            member=GymMember.objects.get(id=id)

        except GymMember.DoesNotExist:
            raise ValueError({"memeber doesn't exist "})    
        
        member.expiry_date+=timedelta(days=extension)
        member.save()

        return member

    