from django.urls import path
from . import views

urlpatterns = [
    path('', views.groups_home, name='groups_home'),  # Головна сторінка груп
    path('group1/', views.group1, name='group1'),
    path('group2/', views.group2, name='group2'),
    path('group3/', views.group3, name='group3'),
    path('group4/', views.group4, name='group4'),
]
