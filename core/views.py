from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer



from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignUpSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# تسجيل مستخدم جديد
class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# تسجيل دخول مستخدم للحصول على توكن JWT
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({"access": str(refresh.access_token)}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

