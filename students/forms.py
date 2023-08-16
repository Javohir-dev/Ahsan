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

class StudentUpdateForm(forms.ModelForm):

    class Meta:
        model = Students
        fields = ["first_name", "last_name", "phone", "subject", "teacher", "price", "month", "status"]


# Create Add Students Form
# class AddStudentsForm(forms.ModelForm):
# 	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
# 	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
# 	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone number", "class":"form-control"}), label="")
# 	subject = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Subject", "class":"form-control"}), label="")
# 	teacher = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Teacher", "class":"form-control"}), label="")
# 	price = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Price", "class":"form-control"}), label="")
# 	month = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Month", "class":"form-control"}), label="")
# 	status = forms.ChoiceField()

# 	class Meta:
# 		model = Students
# 		exclude = ("user",)


# class AddStudentForm(forms.ModelForm):
#     class Meta:
#         model = Students
#         fields = ("first_name", "last_name", "phone", "subject", "teacher", "price", "month", "status")

#     def save(self, commit=True):
#         student = super().save(commit)
#         student.save()

#         return student