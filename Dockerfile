FROM python:3.10.6-buster

COPY requirements.txt /requirements.txt
COPY better_letter /better_letter

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn better_letter.API.fast:app --host 0.0.0.0

#docker docker build --tag=$GAR_IMAGE:translator .
#docker run -it -e PORT=8000 -p 8000:8000 $GAR_IMAGE:translator sh
#docker run -e PORT=8000 -p 8000:8000 --env-file /Users/terezka/code/katia-si/better-letter-API/.env $GAR_IMAGE:translator


