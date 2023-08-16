from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import ListView

from users.forms import UserCreateForm

from students.models import Studens



class StudensListView(ListView):
    def get(self, request):
        students_list = Studens.objects.all()
        context = {
            "students": students_list,
        }

        return render(request, 'students/list.html', context)

