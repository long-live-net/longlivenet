FROM python:3
MAINTAINER ngzm<nk.ngzm@gmail.com>

# setup apt
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y sqlite3
#
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/sitebase
#
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./sitebase /code/sitebase
COPY setup.sh /code/sitebase
#
WORKDIR /code/sitebase
RUN python manage.py collectstatic --no-input
# start application
EXPOSE 8008
CMD ["uwsgi", "--ini", "/code/sitebase/sitebase.ini"]
