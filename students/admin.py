from django.contrib import admin
from students.models import Students, Subjects, Teachers, Months


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone", "teacher", "subject", "created_at", "status"]
    list_filter = ["status", "teacher", "subject"]
    search_fields = ["first_name", "last_name", "subject", "teacher"]
    ordering = ["status", "created_at"]


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone", "subject"]
    list_filter = ["subject"]
    search_fields = ["first_name", "last_name", "subject"]


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(Months)
class MonthsAdmin(admin.ModelAdmin):
    list_display = ["name",]

