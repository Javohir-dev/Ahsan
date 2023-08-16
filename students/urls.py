from django.urls import path

from students.views import StudensListView

app_name = "students"
urlpatterns = [
    path('list/', StudensListView.as_view(), name="students_list"),
]