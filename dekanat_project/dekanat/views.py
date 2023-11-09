from django.shortcuts import render
from .models import Student, Teacher, SessionResult
from .serializers import StudentSerializer, TeacherSerializer, SessionResultSerializer
from rest_framework import generics


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class SessionResultListCreateView(generics.ListCreateAPIView):
    queryset = SessionResult.objects.all()
    serializer_class = SessionResultSerializer

# Create your views here.
