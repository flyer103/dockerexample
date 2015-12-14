FROM ruby
MAINTAINER flyer <flyer103@gmail.com>

RUN gem install redis

COPY redis-trib.rb /

ENTRYPOINT ["/redis-trib.rb"]
