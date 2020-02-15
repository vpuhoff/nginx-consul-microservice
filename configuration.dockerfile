FROM ubuntu:trusty

VOLUME /etc/consul-template/templates
VOLUME /etc/consul-template/conf

COPY conf/* /etc/consul-template/conf/
COPY conf/* /etc/config/
COPY templates/* /etc/consul-template/templates/

CMD tail -f /dev/null