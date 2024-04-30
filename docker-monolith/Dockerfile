from ubuntu:18.04

RUN apt-get update
RUN apt-get install -y git mongodb-server ruby-full ruby-dev build-essential
RUN gem install bundler -v '~> 1.16.1'
RUN git clone -b monolith https://github.com/express42/reddit.git

COPY mongod.conf /etc/mongod.conf
COPY db_config /reddit/db_config
COPY start.sh /start.sh

RUN cd /reddit && rm Gemfile.lock && bundle install
RUN chmod +x /start.sh

CMD ["/start.sh"]
