from __future__ import unicode_literals
from django.shortcuts import render
from .forms import DownloadForm
import youtube_dl
from .models import History
import os
# Create your views here.


def download(request):
    form = DownloadForm(request.POST or None)
    if form.is_valid():
        url = form.cleaned_data.get('url')
        options = {'format': 'best'}
        with youtube_dl.YoutubeDL(options) as youtube:
            dir = os.getcwd()
            if not os.path.exists(dir + '/movies'):
                os.makedirs(dir + '/movies')
                os.chdir(dir + '/movies')
                info = youtube.extract_info(url)
                h = History(url=url)
                h.save()
                os.chdir(dir)
            # response = HttpResponse(content_type='application/force-download')
            # response['Content-Disposition'] = 'attachment; filename="{}.{}"'.format(info['title'], info['ext'])
            # return response
        return render(request, 'downloader/index.html', {'form': form, 'success': '{} was successfully downloaded'.format(info['title'])})
    return render(request, 'downloader/index.html', {'form': form})


