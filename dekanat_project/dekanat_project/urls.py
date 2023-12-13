"""
URL configuration for dekanat_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import SpecialtyListCreateView, SpecialtyDetailView, \
    CourseListCreateView, CourseDetailView, \
    GroupListCreateView, GroupDetailView, \
    StudentListCreateView, StudentDetailView, \
    TeacherListCreateView, TeacherDetailView, \
    SessionResultListCreateView, SessionResultDetailView, RegistrationView

urlpatterns = [
    path('specialties/', SpecialtyListCreateView.as_view(), name='specialty-list-create'),
    path('specialties/<int:pk>/', SpecialtyDetailView.as_view(), name='specialty-detail'),

    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

    path('groups/', GroupListCreateView.as_view(), name='group-list-create'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),

    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),

    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),

    path('session-results/', SessionResultListCreateView.as_view(), name='session-result-list-create'),
    path('session-results/<int:pk>/', SessionResultDetailView.as_view(), name='session-result-detail'),

    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dekanat.urls')),  # Включення URL маршрутизатора вашого додатку
]

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # ...
]
