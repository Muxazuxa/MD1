from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import DownloadForm
import youtube_dl
# Create your views here.


def download(request):
    form = DownloadForm(request.POST or None)
    if form.is_valid():
        url = form.cleaned_data.get('url')
        options = {'format': 'best'}
        with youtube_dl.YoutubeDL(options) as youtube:
            info = youtube.extract_info(url, download=False)
            url = info['url']
        return redirect(url)
    return render(request, 'downloader/index.html', {'form': form})


