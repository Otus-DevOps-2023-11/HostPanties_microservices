FROM ruby:2.2.10-alpine

RUN apk update \
  && apk add build-base

ENV APP_HOME /app
ENV COMMENT_DATABASE_HOST comment_db
ENV COMMENT_DATABASE comments

WORKDIR $APP_HOME 
COPY . $APP_HOME/
RUN bundle install 
RUN bundle update bson
RUN bundle install

CMD ["puma"]
