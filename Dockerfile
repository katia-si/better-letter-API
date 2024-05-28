FROM python:3.10.6-buster

COPY requirements.txt /requirements.txt
COPY package/package #edit name fo our package

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install .

CMD uvicorn mlops.fast:app --host 0.0.0.0 --port $PORT
