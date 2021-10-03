FROM ubuntu:16.04
      
LABEL author="Azizul Hakim Shakil (azizulhakim.shakil18@gmail.com)"

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y openssh-server build-essential wget make python gcc sshpass

RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN wget -O mcperf.tar.gz https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/twemperf/mcperf-0.1.1.tar.gz
RUN mkdir mcperf && tar -xvf mcperf.tar.gz --strip-components=1  -C ./mcperf/
RUN cd /mcperf && ./configure && make && make install

RUN wget -O dude.tar.gz https://bitbucket.org/db7/dude/get/v3.1.tar.gz && mkdir dude && tar -xvf dude.tar.gz --strip-components=1 -C ./dude/
RUN cd /dude && python setup.py install

RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

RUN sed -i 's/22/10023/' /etc/ssh/sshd_config

RUN apt-get -y install r-base

RUN echo 'screencast' > sshpass.txt && chmod 777 sshpass.txt

#sshpass -p screencast ssh -o StrictHostKeyChecking=no root@172.19.0.2
#sshpass -f sshpass.txt ssh root@172.19.0.2 

RUN mkdir a2p05
COPY Benchmark.py /a2p05/
COPY Dudefile /a2p05/
COPY graphs.R /a2p05/
COPY run.sh /a2p05/

WORKDIR /a2p05/

RUN chmod 777 *

EXPOSE 10023

CMD ["/usr/sbin/sshd", "-D"]
