from django.urls import path

from . import views

urlpatterns = [
    path('add_student/', views.add_student, name='student'),
    path('add_student', views.add_student, name='add_student'),
    path('list_student', views.list_student, name='list_student'),
    path('update_student/<int:student_id>/', views.update_student, name='update_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('add_speciality', views.add_speciality, name='add_speciality'),
    path('list_speciality', views.list_speciality, name='list_speciality'),
    path('update_speciality/<int:speciality_id>/', views.update_speciality, name='update_speciality'),
    path('delete_speciality/<int:speciality_id>/', views.delete_speciality, name='delete_speciality'),
    path('add_module', views.add_module, name='add_module'),
    path('list_module', views.list_module, name='list_module'),
    path('update_module/<int:module_id>/', views.update_module, name='update_module'),
    path('delete_module/<int:module_id>/', views.delete_module, name='delete_module'),
]
