FROM golang:1.5
MAINTAINER flyer <flyer103@gmail.com>

# install java-1.8
RUN apt-get update && apt-get install -y unzip && rm -rf /var/lib/apt/lists/*
RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main' > /etc/apt/sources.list.d/jessie-backports.list
ENV LANG C.UTF-8
ENV JAVA_VERSION 8u66
ENV JAVA_DEBIAN_VERSION 8u66-b17-1~bpo8+1

# see https://bugs.debian.org/775775
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872
ENV CA_CERTIFICATES_JAVA_VERSION 20140324

RUN set -x \
	&& apt-get update \
	&& apt-get install -y \
		openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \
		ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \
	&& rm -rf /var/lib/apt/lists/*

# see CA_CERTIFICATES_JAVA_VERSION notes above
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
ENV PATH $PATH:${JAVA_HOME}/bin

RUN mkdir /project
WORKDIR /project

COPY docker-entrypoint.sh /project/
