from django.urls import path

from students.views import (
    StudensListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    delete_student,
)

app_name = "students"
urlpatterns = [
    path('list/', StudensListView.as_view(), name="students_list"),
    path('add/', StudentCreateView.as_view(), name="add"),
    path('detail/<int:id>/', StudentDetailView.as_view(), name="detail"),
    path('update/<int:id>/', StudentUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', delete_student, name="delete"),
]