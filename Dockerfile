FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /downloader
WORKDIR /downloader
ADD . /downloader/
RUN pip3 install -r requirements.txt