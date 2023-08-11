from django.contrib import admin
from django.urls import path,include
from .views import RegisterStudent,ListStudent,DeleteStudent,UpdateStudent,DetailStudent

urlpatterns = [
    path('register/',RegisterStudent.as_view(),name="registerstudent"),
    path('list/',ListStudent.as_view(),name="liststudent"),
    path('delete/<int:pk>',DeleteStudent.as_view(),name="deletestudent"),
    path('update/<int:pk>',UpdateStudent.as_view(),name="updatestudent"),
    path('detail/<int:pk>',DetailStudent.as_view(),name="detailstudent"),
]