FROM python:3.10.6-buster

COPY better_letter /better_letter
COPY requirements.txt /requirements.txt
COPY setup.py /setup.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn better_letter.API.fast:app --host 0.0.0.0 --port $PORT