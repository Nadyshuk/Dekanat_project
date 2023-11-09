from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class StudentTests(TestCase):
    def test_get_students(self):
        url = reverse('student-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class StudentTests(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name='John Doe', email='john@example.com')

    def test_update_student(self):
        url = reverse('student-detail', kwargs={'pk': self.student.pk})
        data = {'name': 'Jane Doe', 'email': 'jane@example.com'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Jane Doe')
        self.assertEqual(response.data['email'], 'jane@example.com')

    def test_delete_student(self):
        url = reverse('student-detail', kwargs={'pk': self.student.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# Create your tests here.
