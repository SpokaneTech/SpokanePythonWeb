# === STAGE 1: Build dependencies in a virtual environment ===
FROM python:3.12-alpine AS builder

WORKDIR /app

# Install build dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev

COPY pyproject.toml /app/

# Install pip-tools and create a virtual environment
RUN pip install --upgrade pip
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip install .[docker]


# === STAGE 2: Runtime with only necessary files ===
FROM python:3.12-alpine

ARG IMAGE_TAG=dev
ENV IMAGE_TAG=${IMAGE_TAG}


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install minimal runtime dependencies
RUN apk add --no-cache libffi openssl libstdc++

# Copy the virtual environment from the builder stage
COPY --from=builder /venv /venv

# Add the virtual environment's Python to the PATH
ENV PATH="/venv/bin:$PATH"

# Copy Django project code
COPY src/django_project /app/
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]