FROM python:3.7

RUN mkdir /app
WORKDIR /app

COPY ./app/ .
RUN pip install -r requirements.txt

CMD [ "gunicorn", "--workers=2", "--threads=1", "app:app", "--preload", "--timeout 10"]