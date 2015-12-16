FROM python:3.5
MAINTAINER flyer <flyer103@gmail.com

VOLUME ["/data/py-pkg/"]

ENV PIPLOCATION "/data/py-pkg/"
ENV PYTHONPATH ${PIPLOCATION}/lib/python3.5/site-packages/
ENV PATH ${PIPLOCATION}/bin/:$PATH

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
