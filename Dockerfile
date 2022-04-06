FROM ubuntu:latest

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt

RUN apt-get install -y pandoc
RUN apt-get install -y vim

COPY src /src
COPY documentation /documentation

RUN chmod +x /src/convert_all.sh
#RUN sed $'s/\r$//' /src/convert_all.sh
#RUN sed $'s/\r$//' /src/convert.sh

ENTRYPOINT ["sh", "/src/convert_all.sh"]