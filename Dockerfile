FROM harbor.nicleary.com/dockerhub/library/python:3.11

WORKDIR /cbt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

RUN apt update && apt upgrade -y
RUN apt install libffi-dev libnacl-dev python3-dev emacs -y

COPY app/requirements.txt .
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt

COPY ./app/cbt .
