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
        try:
            with youtube_dl.YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
                return render(request, 'downloader/index.html', {'form': form, 'success': '{} was successfully downloaded'.format(info['title'])})
        except:
            return render(request, 'downloader/index.html', {'form': form, 'error': 'Enter a valid URL'})
    return render(request, 'downloader/index.html', {'form': form})


