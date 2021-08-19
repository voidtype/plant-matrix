FROM python:3

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python --version
RUN apt update
RUN apt install -y postgresql-client build-essential
RUN apt install -y libpq-dev musl-dev
RUN pip install -r requirements.txt
RUN django-admin startproject backend .
#COPY backend/settings.py /usr/src/app/backend/
RUN echo "ALLOWED_HOSTS = ['144.202.8.17','localhost','127.0.0.1']" >> /usr/src/app/backend/settings.py
RUN echo "DEBUG = False" >> /usr/src/app/backend/settings.py
COPY . .

RUN adduser --disabled-password --no-create-home app
USER app
EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
