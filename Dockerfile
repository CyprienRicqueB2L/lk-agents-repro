FROM python:3.12-slim

# Prevents Python from writing pyc files
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/home/appuser" \
    --shell "/sbin/nologin" \
    --uid "${UID}" \
    appuser

RUN apt-get update && \
    apt-get install -y \
    gcc \
    g++ \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*


USER appuser

RUN mkdir -p /home/appuser/.cache
RUN chown -R appuser /home/appuser/.cache

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest==8.3.5 pytest-asyncio==0.26.0 pytest_async==0.1.1

COPY . .


RUN python -m a1 download-files
