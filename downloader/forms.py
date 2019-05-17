from django import forms
from .models import History


class DownloadForm(forms.ModelForm):
    url = forms.URLField(max_length=200, required=True)

    class Meta:
        model = History
        fields = ('url',)

