FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY euphoria/ .

CMD ["gunicorn", "config.wsgi:application", "--bind", "0:8000"]

