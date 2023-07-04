FROM openjdk:11-jdk-headless

RUN apt-get update && apt-get install -y unzip

RUN mkdir -p /opt/mango

ENV mango_paths_home /opt/mango

RUN useradd --system --home-dir /opt/mango --shell /bin/false mango

# Coloque o arquivo zip do Mango na mesma pasta deste Dockerfile
COPY enterprise-m2m2-core-4.0.0.zip /tmp/

# Descompacta o arquivo zip do Mango e define as permissões corretas
RUN unzip /tmp/enterprise-m2m2-core-4.0.0.zip -d /opt/mango \
    && chown -R mango:mango /opt/mango \
    && rm /tmp/enterprise-m2m2-core-4.0.0.zip

# Copia o arquivo de configuração do Mango para o diretório correto
COPY mango.properties /opt/mango/mango.properties

# Copia o script de opções de inicialização do Java para o diretório correto
COPY start-options.sh /opt/mango/bin/start-options.sh

# Define o diretório de trabalho
WORKDIR /opt/mango

# Define o usuário "mango" como usuário padrão para execução do contêiner
USER mango

# Define o comando a ser executado quando o contêiner for iniciado
CMD ["bin/start-mango.sh"]
