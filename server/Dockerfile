# Use an official Python runtime as a parent image
FROM python:3.9

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBUG=0

# Install Python dependencies
RUN apt-get update && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev
COPY requirements.txt /app/
RUN python -m pip install --no-cache-dir --upgrade pip -r requirements.txt

# copy project
COPY . /app

EXPOSE 8000

# CMD [ "/bin/ls", "-l"]
# CMD python manage.py migrate --settings imago.settings
# CMD python manage.py runserver 0.0.0.0:8000 --settings imago.settings
