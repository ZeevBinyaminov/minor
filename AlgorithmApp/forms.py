from django import forms
from .models import Place


class UploadForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('number',)
