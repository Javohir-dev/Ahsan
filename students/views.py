from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from config.cutom_permission import OnlySuperUsers

from students.forms import StudentUpdateForm

from students.models import Students, Teachers, Subjects, Months



# class StudensListView(ListView):
#     template_name = 'students/list.html'
#     queryset = Students.objects.all()
#     context_object_name = 'all_students'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["students"] = Students.active.all()

#         return context


from django.db.models import Q

class StudensListView(ListView):
    def get(self, request):
        students = Students.objects.all().order_by('id')
        page_size = request.GET.get('page_size', 10)
        paginator = Paginator(students, page_size)

        page_num = request.GET.get('page', 1)
        page_object = paginator.get_page(page_num)
        search_query = request.GET.get('search', '')
        if search_query:
            students = students.filter(
                Q(first_name__icontains=search_query) |  # first_name yoki
                Q(last_name__icontains=search_query)
            )

            paginator = Paginator(students, page_size)  # Paginator ni qayta o'rnatish kerak
            page_object = paginator.get_page(page_num)

        context = {
            "page_obj": page_object,
            "search_query": search_query,
        }

        return render(request, 'students/list.html', context)


class NoActiveStudensListView(ListView):
    template_name = 'students/no-active-list.html'
    queryset = Students.objects.all()
    context_object_name = 'all_students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Students.disable.all()

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
    form_class = StudentUpdateForm
    template_name = "students/update.html"
    pk_url_kwarg = 'id'
    context_object_name = 'student'
    # reverse_lazy = "students:student_list"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teachers"] = Teachers.objects.all()
        context["subjects"] = Subjects.objects.all()
        context["months"] = Months.objects.all()

        return context

    def get_success_url(self):
        return reverse_lazy("students:student_detail", kwargs={"id": self.object.id})


def delete_student(request, pk):
    delete_student = Students.objects.get(id=pk)
    delete_student.delete()

    return redirect("students:students_list")

