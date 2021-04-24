# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONBUFFERED=1
WORKDIR /home/code
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY /Starcounter /home/code
