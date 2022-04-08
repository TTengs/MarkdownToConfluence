FROM ubuntu:latest

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt

RUN apt-get install -y pandoc
RUN apt-get install -y vim

COPY ./src /script

RUN chmod +x /script/convert_all.sh
RUN chmod +x /script/convert.sh
RUN sed $'s/\r$//' /script/convert_all.sh
RUN sed $'s/\r$//' /script/convert.sh

ENTRYPOINT ["sh", "/script/convert_all.sh"]