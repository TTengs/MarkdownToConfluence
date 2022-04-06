FROM ubuntu:latest

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt

RUN apt-get install -y pandoc

COPY src /src
COPY documentation /documentation

RUN chmod +x /src/convert_all.sh

ENTRYPOINT ["/src/convert_all.sh"]