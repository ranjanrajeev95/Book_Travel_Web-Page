FROM python:3.9.4

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
