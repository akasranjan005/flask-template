FROM python:3.6-slim-jessie

LABEL maintainer="Akash Ranjan" email="akashdeveloper005@gmail.com"

RUN apt-get -y update && apt-get install -yq supervisor

COPY ./src/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY ./src/ /home/src/
WORKDIR /home/src/

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENV ENV=production

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
