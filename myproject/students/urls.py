from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_home, name='students_home'),  # Головна сторінка
    path('student1/', views.student1, name='student1'),
    path('student2/', views.student2, name='student2'),
    path('student3/', views.student3, name='student3'),
    path('student4/', views.student4, name='student4'),
]
