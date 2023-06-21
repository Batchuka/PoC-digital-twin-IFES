# Define a imagem base
FROM debian:bullseye-20211201

# Copia todo o conteúdo do diretório atual para a pasta /workdir dentro do container
COPY . /workdir

# Define a pasta de trabalho padrão
WORKDIR /workdir

# Cria uma pasta chamada /persistent que será usada para armazenar arquivos persistentes
RUN mkdir /persistent

# Define um volume /persistent para que os arquivos armazenados nesta pasta persistam mesmo após a reinicialização do container
VOLUME /persistent

# Executa o script de instalação (openplc) especificado no arquivo install.sh, passando "docker" como parâmetro
RUN ./install.sh docker

# Cria um arquivo vazio chamado mbconfig.cfg na pasta /persistent
RUN touch /persistent/mbconfig.cfg

# Cria um arquivo vazio chamado persistent.file na pasta /persistent
RUN touch /persistent/persistent.file

# Cria uma pasta chamada /persistent/st_files que será usada para armazenar as as lógicas de controlador a serem executadas no openplc runtime
RUN mkdir /persistent/st_files

# Copia o arquivo openplc.db da pasta /workdir/webserver para a pasta /persistent
RUN cp /workdir/webserver/openplc.db /persistent/openplc.db

# Renomeia o arquivo openplc.db da pasta /workdir/webserver para openplc_default.db — para manter um backup do banco inicial
RUN mv /workdir/webserver/openplc.db /workdir/webserver/openplc_default.db

# Copia o arquivo dnp3.cfg da pasta /workdir/webserver para a pasta /persistent
RUN cp /workdir/webserver/dnp3.cfg /persistent/dnp3.cfg

# Renomeia o arquivo dnp3.cfg da pasta /workdir/webserver para dnp3_default.cfg
RUN mv /workdir/webserver/dnp3.cfg /workdir/webserver/dnp3_default.cfg

# Copia todos os arquivos na pasta /workdir/webserver/st_files para a pasta /persistent/st_files
RUN cp /workdir/webserver/st_files/* /persistent/st_files

# Renomeia a pasta st_files da pasta /workdir/webserver para st_files_default
RUN mv /workdir/webserver/st_files /workdir/webserver/st_files_default

# Cria um link simbólico de mbconfig.cfg na pasta /persistent para a pasta /workdir/webserver/mbconfig.cfg
RUN ln -s /persistent/mbconfig.cfg /workdir/webserver/mbconfig.cfg

# Cria um link simbólico de persistent.file na pasta /persistent para a pasta /workdir/webserver/persistent.file
RUN ln -s /persistent/persistent.file /workdir/webserver/persistent.file

# Cria um link simbólico de openplc.db na pasta /persistent para a pasta /workdir/webserver/openplc.db
RUN ln -s /persistent/openplc.db /workdir/webserver/openplc.db

# Cria um link simbólico de dnp3.cfg na pasta /persistent para a pasta /workdir/webserver/dnp3.cfg
RUN ln -s /persistent/dnp3.cfg /workdir/webserver/dnp3.cfg

# Cria um link simbólico de st_files na pasta /persistent para a pasta /workdir/webserver/st_files
RUN ln -s /persistent/st_files /workdir/webserver/st_files

EXPOSE 8080

# Define o comando de entrada do container como o arquivo start_openplc.sh presente na pasta /workdir
ENTRYPOINT ["./webserver/scripts/start_openplc.sh"]
