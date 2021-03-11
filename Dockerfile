FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app/ /app/
<<<<<<< HEAD
=======

RUN pip install -r requirements.txt
>>>>>>> main
