FROM ubuntu:jammy

RUN apt update -y && apt install -y wget gnupg

# Import GPG key for MySQL APT repository
RUN wget https://dev.mysql.com/doc/mysql-apt-repo-0.9.0-1_all.deb \
    && dpkg -i mysql-apt-repo-0.9.0-1_all.deb \
    && apt update -y

# Install MySQL Server
RUN echo "mysql-community-server mysql-community-server/root-pass password root" | debconf-set-selections \
    && echo "mysql-community-server mysql-community-server/re-root-pass password root" | debconf-set-selections \
    && apt install -y mysql-server

# Cleanup
RUN apt clean

EXPOSE 3306 33060 33061 8080

CMD ["tail", "-f", "/dev/null"]