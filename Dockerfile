FROM python:3

ENV PYTHONIOENCODING UTF-8
ENV PYTHONUNBUFFERED=1


ENV TZ=Asia/Bishkek

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt



