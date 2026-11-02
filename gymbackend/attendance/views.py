from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions,generics
from .serializers import AttendanceSerializer,AttendanceDateSerializers
from .models import AttendanceModel
from account.models import GymMember

from datetime import datetime,date


class MarkAttendanceView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # user must be logged in

    def get(self, request):
        try:
            # Get the gym member linked to the logged-in user
            gym_member = GymMember.objects.get(user=request.user)
        except GymMember.DoesNotExist:
            return Response(
                {"error": "No GymMember profile found for this user."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if attendance already marked for today
        today = date.today()
        if AttendanceModel.objects.filter(member=gym_member, date=today).exists():
            record = AttendanceModel.objects.get(member=gym_member, date=today)
            return Response(
                {
                    "message": "Attendance already marked for today.",
                    "data": AttendanceSerializer(record).data
                },
                status=status.HTTP_200_OK
            )

        # Mark new attendance
        data = {
            "member": gym_member.id,
            "status": "P"  # default as Present
        }
        serializer = AttendanceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Attendance marked successfully.", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




from datetime import datetime
from rest_framework import generics, permissions
from .models import AttendanceModel
from .serializers import AttendanceSerializer

class GetAttendance(generics.ListAPIView):
    serializer_class = AttendanceDateSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        member = self.request.user.gym_profile

        # Get query parameters
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')

        # Default to current month if not provided
        if not (month and year):
            today = datetime.today()
            month, year = today.month, today.year

        # ✅ Correct double underscore syntax
        queryset = AttendanceModel.objects.filter(
            member=member,
            date__month=month,
            date__year=year
        ).order_by('date')

        return queryset

