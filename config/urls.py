from django.contrib import admin
from django.urls import path, include
from .views import home_page

urlpatterns = [
    path('', home_page, name="home"),
    path('users/', include('users.urls')),

    path('admin/', admin.site.urls),
]
