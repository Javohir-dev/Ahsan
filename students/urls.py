from django.urls import path

from students.views import (
    StudensListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    NoActiveStudensListView,
    delete_student,
)

app_name = "students"
urlpatterns = [
    path('no-actives/', NoActiveStudensListView.as_view(), name="no_actives"),
    path('list/', StudensListView.as_view(), name="students_list"),
    path('add/', StudentCreateView.as_view(), name="student_add"),
    path('detail/<int:id>/', StudentDetailView.as_view(), name="student_detail"),
    # path('update/<int:id>/', StudentUpdateView.as_view(), name="update"),
    path('students/<int:id>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('delete/<int:pk>/', delete_student, name="delete"),
]