# gym/views.py
from rest_framework import generics, permissions,status
from rest_framework.response import Response
    
from rest_framework.authentication import TokenAuthentication
from .serializers import RegisterSerializer, GymMemberSerializer
from .models import GymMember

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
class LogoutView(generics.RetrieveAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        request.user.auth_token.delete()
        return Response({"message":"you sucessfully logged out "},status=status.HTTP_200_OK)
    
    

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = GymMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.gym_profile
