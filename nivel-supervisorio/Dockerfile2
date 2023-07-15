FROM amazoncorretto:17

RUN yum update -y && yum install unzip systemd -y

RUN mkdir -p /root

ENV mango_paths_home /root

COPY free-m2m2-core-5.0.2.zip /tmp/

RUN unzip /tmp/free-m2m2-core-5.0.2.zip -d /root && rm /tmp/free-m2m2-core-5.0.2.zip

WORKDIR /root

RUN cp /root/bin/mango.service /etc/systemd/system/
# Copia o arquivo "mango.service" para o diretório "/etc/systemd/system/" dentro do contêiner

EXPOSE 8080

RUN systemctl enable mango
# Habilita o serviço "mango" para iniciar durante a inicialização do sistema

CMD ["/sbin/init"]
# Inicia o sistema init (systemd) para gerenciar os serviços no contêiner