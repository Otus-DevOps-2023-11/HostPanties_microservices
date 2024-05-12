FROM fluent/fluentd:v1.16

USER root
RUN gem install fluent-plugin-elasticsearch \
  && gem install fluent-plugin-grok-parser 
ADD fluent.conf /fluentd/etc 
USER fluent
