from __future__ import unicode_literals
from django.shortcuts import render
from .forms import DownloadForm
import youtube_dl

# Create your views here.


def download(request):
    form = DownloadForm(request.POST or None)
    if form.is_valid():
        url = form.cleaned_data.get('url')
        options = {'format': 'best'}
        with youtube_dl.YoutubeDL(options) as youtube:
            info = youtube.extract_info(url)
        return render(request, 'downloader/index.html', {'form': form, 'success': '{} was successfully downloaded'.format(info['title'])})
    return render(request, 'downloader/index.html', {'form': form})


