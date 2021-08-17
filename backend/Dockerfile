FROM python:3

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python --version
RUN pip install -r requirements.txt
RUN django-admin startproject backend .
RUN echo "ALLOWED_HOSTS = ['144.202.8.17']" >> /usr/src/app/backend/settings.py
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
