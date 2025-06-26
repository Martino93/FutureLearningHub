# Use official Python image as base
FROM python:3.12-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev nodejs npm && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements (use environment.yml for conda, requirements.txt for pip)
COPY environment.yml /app/

# Install pip and conda dependencies
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv lock --requirements > requirements.txt || true && \
    pip install -r requirements.txt

# Copy the rest of the code
COPY . /app/

# Collect static files (for Django)
RUN python tutoring_platform/manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Start server
CMD ["python", "tutoring_platform/manage.py", "runserver", "0.0.0.0:8000"]