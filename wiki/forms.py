from django import forms
from wiki.models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'author', 'content']
