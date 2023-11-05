from django import forms
from .models import Algo


class UploadForm(forms.ModelForm):
    class Meta:
        model = Algo
        fields = ('number_A', 'number_B', 'number_C')
