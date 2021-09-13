FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /students-api

COPY requirements.txt .
COPY alembic.ini .
COPY main.py .
COPY app/ ./app/
COPY migrations/ ./migrations/
COPY docker/entrypoint.sh .

RUN pip install -r requirements.txt --no-cache-dir

CMD ["./entrypoint.sh"]