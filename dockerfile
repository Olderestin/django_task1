FROM python:3.10.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/temp/

RUN pip install --upgrade pip
RUN pip install -r /app/temp/requirements.txt

WORKDIR /app/
COPY . /app/