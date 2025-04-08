# Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies including Node.js + npm
RUN apt-get update \
  && apt-get install -y build-essential libpq-dev curl netcat-openbsd gnupg unzip \
  && curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 \
  && chmod +x tailwindcss-linux-x64 \
  && mv tailwindcss-linux-x64 /usr/local/bin/tailwindcss \
  && pip install --upgrade pip

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all project files
COPY . .

# Entrypoint for collectstatic and migration
ENTRYPOINT ["/app/entrypoint.sh"]

