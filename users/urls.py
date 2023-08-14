from django.urls import path

from .views import RegisterView, LoginView

app_name = "users"
urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
]