FROM python:3.10-slim

COPY better_letter /better_letter
COPY requirements.txt /requirements.txt
COPY setup.py /setup.py

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    tesseract-ocr-deu \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install .

CMD uvicorn better_letter.API.fast:app --host 0.0.0.0 --port $PORT
