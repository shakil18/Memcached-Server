FROM ubuntu:16.04
      
MAINTAINER Azizul Hakim Shakil <Azizul_Hakim.Shakil@mailbox.tu-dresden.de>

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y openssh-server libevent-dev build-essential wget make

RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN wget -O memcached-1.4.33.tar.gz http://www.memcached.org/files/memcached-1.4.33.tar.gz
RUN mkdir memcached && tar -xzf memcached-1.4.33.tar.gz --strip-components=1  -C ./memcached/
RUN cd /memcached && ./configure --build="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" && make -j "$(nproc)" && make install

RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22 11211

CMD ["/usr/sbin/sshd", "-D"]











