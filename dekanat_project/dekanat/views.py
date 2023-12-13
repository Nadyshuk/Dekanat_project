from django.shortcuts import render
from rest_framework import generics
from .models import Specialty, Course, Group, Student, Teacher, SessionResult
from .serializers import SpecialtySerializer, CourseSerializer, GroupSerializer, \
    StudentSerializer, TeacherSerializer, SessionResultSerializer, UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class SpecialtyListCreateView(generics.ListCreateAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer

class SpecialtyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SessionResultListCreateView(generics.ListCreateAPIView):
    queryset = SessionResult.objects.all()
    serializer_class = SessionResultSerializer

class SessionResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SessionResult.objects.all()
    serializer_class = SessionResultSerializer

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def validate_username(self, value):
        # Перевірка унікальності імені користувача
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Це ім'я користувача вже використовується.")
        return value

    def validate_password(self, value):
        # Перевірка деяких умов для пароля
        if len(value) < 8:
            raise serializers.ValidationError("Пароль повинен містити принаймні 8 символів.")
        return value

class UserLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                login(request, user)
                return Response({'token': user.auth_token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        # Тут реалізація вашого вигляду для адміністраторів
        return Response({'message': 'Only admins can access this view'}, status=status.HTTP_200_OK)
# Create your views here.
