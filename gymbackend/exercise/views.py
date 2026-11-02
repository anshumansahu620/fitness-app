# exercise/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import ExerciseLog
from .serializers import ExerciseLogSerializer

class ExerciseLogCreateView(generics.CreateAPIView):
    """
    Create a new exercise log for the authenticated GymMember.
    """
    serializer_class = ExerciseLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        # Pass request to serializer to auto-set member
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class ExerciseLogDeleteView(generics.DestroyAPIView):
    """  
    Delete an exercise log (only if it belongs to the logged-in GymMember).
    """
    serializer_class = ExerciseLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'log_id'

    def get_queryset(self):
        # Only allow deletion of logs that belong to the logged-in member
        return ExerciseLog.objects.filter(member=self.request.user.gym_profile)

    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ExerciseLog.DoesNotExist:
            return Response(
                {"error": "Exercise log not found or does not belong to you."},
                status=status.HTTP_404_NOT_FOUND
            )

from rest_framework import generics, permissions
from .models import ExerciseLog
from .serializers import ExerciseLogSerializer

class ExerciseLogListView(generics.ListAPIView):
    
    serializer_class = ExerciseLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        member = self.request.user.gym_profile
        queryset = ExerciseLog.objects.filter(member=member)

        # Optional filtering by date
        date_param = self.request.query_params.get('date')
        if date_param:
            queryset = queryset.filter(date=date_param)
        return queryset
