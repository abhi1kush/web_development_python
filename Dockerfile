FROM python:3.7

ARG APP_ENV=local
ENV ENV ${APP_ENV}

RUN apt-get update && apt-get install -y supervisor

RUN apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

ADD requirements.txt /flask_setup/
WORKDIR /flask_setup
RUN pip install -r requirements.txt

ADD . /flask_setup
COPY setup/supervisor.conf /etc/supervisor/conf.d/
ENTRYPOINT ["/usr/bin/supervisord"]
