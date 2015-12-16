FROM python:3.5
MAINTAINER flyer <flyer103@gmail.com

VOLUME ["/data/py-pkg/"]

ENV PIPLOCATION "/data/py-pkg/"

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
