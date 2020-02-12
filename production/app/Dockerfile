FROM python:3
MAINTAINER ngzm<nk.ngzm@gmail.com>

# setup apt
# setup apt
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y sqlite3
#
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/sitebase-on-django
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
#
COPY ./sitebase-on-django /code/sitebase-on-django
WORKDIR /code/sitebase-on-django
RUN python manage.py migrate

# start application
WORKDIR /code
EXPOSE 8008
CMD ["uwsgi", "--ini", "/code/sitebase-on-django/sitebase.ini"]
