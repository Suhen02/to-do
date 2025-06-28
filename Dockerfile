
FROM python:3.12-slim


WORKDIR /app


RUN apt-get update && apt-get install -y gcc libpq-dev


COPY . /app/
COPY .env /app/.env

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python manage.py collectstatic --noinput && \
    python manage.py makemigrations && \
    python manage.py migrate


CMD ["gunicorn", "todoapp.wsgi:application", "--bind", "0.0.0.0:8000"]