from rest_framework import serializers
from .models import Student, Teacher, SessionResult


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'subject']


class SessionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionResult
        fields = ['id', 'student', 'subject', 'grade']
