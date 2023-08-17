from django import forms

from students.models import Students



class StudentsCreateForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ["first_name", "last_name", "phone", "subject", "teacher", "price", "month", "status"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "teacher": forms.TextInput(attrs={"class": "form-control"}),
        }

# class StudentUpdateForm(forms.ModelForm):

#     class Meta:
#         model = Students
#         fields = ["first_name", "last_name", "phone", "subject", "teacher", "price", "month", "status"]


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ["first_name", "last_name", "phone", "subject", "teacher", "price", "month", "status"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
        }

