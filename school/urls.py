from django.urls import path
from . import views

urlpatterns = [
	path('classes', views.classes, name='classes'),
	path('classes/<int:class_id>/', views.student_list_view, name='student_list'),
]