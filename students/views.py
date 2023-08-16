from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from config.cutom_permission import OnlySuperUsers

from students.forms import (
    StudentsCreateForm,
    StudentUpdateForm,
    # AddStudentForm,
    # AddStudentsForm
)

from students.models import Students, Teachers, Subjects, Months



class StudensListView(ListView):
    template_name = 'students/list.html'
    queryset = Students.objects.all()
    context_object_name = 'all_students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Students.active.all()

        return context


class StudentDetailView(DetailView):
    model = Students
    pk_url_kwarg = 'id'
    template_name = 'students/detail.html'
    context_object_name = 'student'


class StudentCreateView(OnlySuperUsers, CreateView):
    template_name = "students/add.html"
    model = Students
    # queryset = 'students'
    fields = ["first_name", "last_name", "phone", "subject", "teacher", "price", "month", "status"]
    success_url = reverse_lazy("students:students_list")


class StudentUpdateView(OnlySuperUsers, UpdateView):
    model = Students
    pk_url_kwarg = 'id'
    template_name = "students/update.html"
    fields = ["first_name", "last_name", "phone", "subject", "teacher", "price", "month", "status"]
    success_url = reverse_lazy("students:students_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teacher"] = Teachers.objects.all()
        context["subject"] = Subjects.objects.all()
        context["month"] = Months.objects.all()

        return context

# class StudentUpdateView(OnlySuperUsers, UpdateView):
#     def get(self, request, id):
#         student_update_form = StudentUpdateForm(instance=request.student)
#         teacher = Teachers.objects.all()
#         subject = Subjects.objects.all()
#         month = Months.objects.all()
#         context = {
#             "form": student_update_form,
#             "teacher": teacher,
#             "subject": subject,
#             "month": month,
#         }

#         return render(request, 'students/update.html', context)
#     def post(self, request, id):
#         student_update_form = StudentUpdateForm(
#             instance=request.student, 
#             data=request.POST,
#         )

#         if student_update_form.is_valid():
#             student_update_form.save()
            
#             return redirect("students:detail")
#         else:
#             return render(request, 'students/students/update.html', {"form": student_update_form})

def delete_student(request, pk):
    delete_student = Students.objects.get(id=pk)
    delete_student.delete()

    return redirect("students:students_list")

