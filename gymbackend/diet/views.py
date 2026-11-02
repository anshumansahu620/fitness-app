from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,permissions, status, permissions
from .models import DietEntry
from .serializers import DietEntrySerializer
from account.models import GymMember

class DietEntryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            gym_member = GymMember.objects.get(user=request.user)
        except GymMember.DoesNotExist:
            return Response({"error": "No GymMember profile found."}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data['member'] = gym_member.id  # attach user automatically

        serializer = DietEntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Diet entry added successfully.", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        gym_member = GymMember.objects.get(user=request.user)
        entries = DietEntry.objects.filter(member=gym_member).order_by('-created_at')
        serializer = DietEntrySerializer(entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DietListView(generics.ListAPIView):
    serializer_class = DietEntrySerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        member=self.request.user.gym_profile
        queryset=DietEntry.objects.filter(member=member)
        date_param=self.request.query_params.get('date')
        if date_param:
            queryset=queryset.filter(date=date_param)

        return queryset
    
