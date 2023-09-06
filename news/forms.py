from django import forms
from news.models import NewsComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = NewsComment
        fields = ["comment"]