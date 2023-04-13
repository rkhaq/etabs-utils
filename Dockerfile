# Dockerfile

FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Copy wait-for-it.sh and make it executable
COPY wait-for-it.sh /app/
RUN chmod +x /app/wait-for-it.sh