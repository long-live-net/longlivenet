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
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./sitebase /code/sitebase
COPY setup.sh /code/sitebase
#
EXPOSE 8008
WORKDIR /code/sitebase
# start application
CMD ["uwsgi", "--ini", "/code/sitebase/sitebase.ini"]
