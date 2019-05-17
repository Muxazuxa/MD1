from django import forms
from .models import History


class DownloadForm(forms.ModelForm):
    url = forms.RegexField(regex=r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+')

    class Meta:
        model = History
        fields = ('url',)

