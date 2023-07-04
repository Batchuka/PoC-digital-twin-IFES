FROM amazoncorretto:17

RUN yum update -y && yum install unzip curl -y

RUN mkdir -p /root

ENV mango_paths_home /root

COPY free-m2m2-core-5.0.2.zip /tmp/

RUN unzip /tmp/free-m2m2-core-5.0.2.zip -d /root && rm /tmp/free-m2m2-core-5.0.2.zip

WORKDIR /root

EXPOSE 8080

ENTRYPOINT ["bin/start-mango.sh"]
