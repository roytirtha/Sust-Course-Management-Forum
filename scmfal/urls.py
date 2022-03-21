from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='course-home'),
    path('courses/', views.course, name='course-about'),
]
