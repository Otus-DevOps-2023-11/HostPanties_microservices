FROM ubuntu:16.04
RUN apt-get update \
 && apt-get install -y ruby-full ruby-dev build-essential \
 && gem install bundler -v '~> 1.16.1' --no-ri --no-rdoc

ENV APP_HOME /app
ENV POST_SERVICE_HOST post
ENV POST_SERVICE_PORT 5000
ENV COMMENT_SERVICE_HOST comment
ENV COMMENT_SERVICE_PORT 9291

WORKDIR $APP_HOME
ADD . $APP_HOME

RUN bundle install

CMD ["puma"]
