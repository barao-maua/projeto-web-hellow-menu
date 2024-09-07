FROM python:3-alpine

COPY . /app

WORKDIR /app

RUN pip install django pillow crispy-bootstrap5

RUN python manage.py migrate

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]P