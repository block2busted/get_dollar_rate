FROM python:3.9.6

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN pip install valutes-protobuf
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
