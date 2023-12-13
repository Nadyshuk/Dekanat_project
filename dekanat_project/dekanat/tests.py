from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Specialty, Course, Group, Student, Teacher, SessionResult
from django.contrib.auth.models import User

class SpecialtyTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.specialty_data = {'name': 'Computer Science', 'code': 'CS', 'department': 'IT'}
        self.specialty = Specialty.objects.create(**self.specialty_data)

    def test_specialty_serializer(self):
        serializer = SpecialtySerializer(data=self.specialty_data)
        self.assertTrue(serializer.is_valid())

    def test_specialty_list_view(self):
        response = self.client.get(reverse('specialty-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Очікуємо одну спеціальність від setUp

    def test_specialty_detail_view(self):
        response = self.client.get(reverse('specialty-detail', args=[self.specialty.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.specialty_data['name'])

class CourseTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course_data = {'name': 'Computer Science', 'code': 'CS101', 'start_date': '2023-01-01', 'end_date': '2023-05-31'}
        self.course = Course.objects.create(**self.course_data)

    def test_course_serializer(self):
        serializer = CourseSerializer(data=self.course_data)
        self.assertTrue(serializer.is_valid())

    def test_course_list_view(self):
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Очікуємо один курс від setUp

    def test_course_detail_view(self):
        response = self.client.get(reverse('course-detail', args=[self.course.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.course_data['name'])

class GroupTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course = Course.objects.create(name='Computer Science', code='CS101', start_date='2023-01-01', end_date='2023-05-31')
        self.group_data = {'name': 'CS101-A', 'course': self.course.id}
        self.group = Group.objects.create(**self.group_data)

    def test_group_serializer(self):
        serializer = GroupSerializer(data=self.group_data)
        self.assertTrue(serializer.is_valid())

    def test_group_list_view(self):
        response = self.client.get(reverse('group-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Очікуємо одну групу від setUp

    def test_group_detail_view(self):
        response = self.client.get(reverse('group-detail', args=[self.group.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.group_data['name'])

class StudentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course = Course.objects.create(name='Computer Science', code='CS101', start_date='2023-01-01', end_date='2023-05-31')
        self.specialty = Specialty.objects.create(name='Computer Science', code='CS', department='CS Department')
        self.group = Group.objects.create(name='CS101-A', course=self.course)
        self.student_data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com', 'group': self.group.id, 'specialty': self.specialty.id, 'course': self.course.id}
        self.student = Student.objects.create(**self.student_data)

    def test_student_serializer(self):
        serializer = StudentSerializer(data=self.student_data)
        self.assertTrue(serializer.is_valid())

    def test_student_list_view(self):
        response = self.client.get(reverse('student-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Очікуємо одного студента від setUp

    def test_student_detail_view(self):
        response = self.client.get(reverse('student-detail', args=[self.student.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.student_data['first_name'])

class TeacherTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.teacher_data = {'first_name': 'John', 'last_name': 'Doe', 'subject': 'Computer Science'}
        self.teacher = Teacher.objects.create(**self.teacher_data)

    def test_teacher_serializer(self):
        serializer = TeacherSerializer(data=self.teacher_data)
        self.assertTrue(serializer.is_valid())

    def test_teacher_list_view(self):
        response = self.client.get(reverse('teacher-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Очікуємо одного вчителя від setUp

    def test_teacher_detail_view(self):
        response = self.client.get(reverse('teacher-detail', args=[self.teacher.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.teacher_data['first_name'])

class SessionResultTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course = Course.objects.create(name='Computer Science', code='CS101', start_date='2023-01-01', end_date='2023-05-31')
        self.specialty = Specialty.objects.create(name='Computer Science', code='CS', department='CS Department')
        self.group = Group.objects.create(name='CS101-A', course=self.course)
        self.student = Student.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com', group=self.group, specialty=self.specialty, course=self.course)
        self.teacher = Teacher.objects.create(first_name='Jane', last_name='Doe', subject='Computer Science')
        self.session_result_data = {'student': self.student.id, 'subject': 'Programming', 'grade': 90.5, 'teacher': self.teacher.id}
        self.session_result = SessionResult.objects.create(**self.session_result_data)

    def test_session_result_serializer(self):
        serializer = SessionResultSerializer(data=self.session_result_data)
        self.assertTrue(serializer.is_valid())

    def test_session_result_list_view(self):
        response = self.client.get(reverse('sessionresult-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Очікуємо один результат сесії від setUp

    def test_session_result_detail_view(self):
        response = self.client.get(reverse('sessionresult-detail', args=[self.session_result.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['subject'], self.session_result_data['subject'])

class UserRegistrationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.registration_data = {'username': 'john_doe', 'password': 'test_password'}
        self.registration_url = reverse('user-registration')

    def test_user_registration_serializer(self):
        serializer = UserRegistrationSerializer(data=self.registration_data)
        self.assertTrue(serializer.is_valid())

    def test_user_registration_view(self):
        response = self.client.post(self.registration_url, data=self.registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username=self.registration_data['username']).exists())

class UserLoginTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'username': 'john_doe', 'password': 'test_password'}
        User.objects.create_user(**self.user_data)
        self.login_data = {'username': 'john_doe', 'password': 'test_password'}
        self.login_url = reverse('user-login')

    def test_user_login_serializer(self):
        serializer = UserLoginSerializer(data=self.login_data)
        self.assertTrue(serializer.is_valid())

    def test_user_login_view(self):
        response = self.client.post(self.login_url, data=self.login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)