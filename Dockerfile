FROM python:3.7
ENV PYTHONUNBUFFERD 1
ENV LANG ja_JP.UTF-8

WORKDIR /app
COPY requirements.txt /app/

RUN pip3 install -r requirements.txt
COPY . /app/

EXPOSE 8000
