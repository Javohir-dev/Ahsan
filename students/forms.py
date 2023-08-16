from django import forms
from users.models import CustomUser

from students.models import Studens


# Create Add Record Form
# class AddRecordForm(forms.ModelForm):
# 	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
# 	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
# 	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")

# 	class Meta:
# 		model = Studens
# 		exclude = ("user",)