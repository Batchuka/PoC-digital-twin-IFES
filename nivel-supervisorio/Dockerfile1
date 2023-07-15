FROM amazoncorretto:17

RUN yum update -y && \
    yum install -y unzip systemd curl wget telnet net-tools procps
# Atualiza e instala pacotes necessários, como unzip, systemd e outras ferramentas de rede e gerenciamento de processos

# Criação do diretório de instalação
RUN mkdir /opt/mango

# Definição da variável de ambiente MA_HOME
ENV MA_HOME /opt/mango

# Criação do usuário "mango"
RUN useradd --system --home-dir /opt/mango --shell /bin/false mango

# Copia do arquivo zip para o diretório de instalação
COPY m2m2-core-3.7.12.zip /tmp/

# Extração do arquivo zip para o diretório de instalação
RUN unzip /tmp/m2m2-core-3.7.12.zip -d /opt/mango && rm /tmp/m2m2-core-3.7.12.zip

# Configuração do dono do diretório de instalação
RUN chown -R mango:mango /opt/mango

# Copia do arquivo env.properties para o diretório de overrides
COPY env.properties /opt/mango/overrides/properties/

# Configuração do arquivo env.properties
# (Você precisará fornecer o arquivo env.properties com as configurações desejadas)
# Exemplo: COPY env.properties /opt/mango/overrides/properties/env.properties

# Copia do script start-options.sh para o diretório de overrides
COPY start-options.sh /opt/mango/overrides/

# Configuração do arquivo start-options.sh
# (Você precisará fornecer o arquivo start-options.sh com as configurações desejadas)
# Exemplo: COPY start-options.sh /opt/mango/overrides/start-options.sh

# Copia do arquivo de serviço do Mango para o systemd
COPY mango.service /etc/systemd/system/

# Definição das permissões corretas para o arquivo de serviço
RUN chown mango:mango /etc/systemd/system/mango.service

# Alteração para o usuário "mango"
USER mango

EXPOSE 8080

CMD ["/sbin/init"]