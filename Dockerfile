FROM ubuntu:latest

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt

RUN apt-get install -y pandoc
RUN apt-get install -y vim

COPY ./MarkdownToConfluence /MarkdownToConfluence

RUN chmod +x /MarkdownToConfluence/convert_all.sh
RUN chmod +x /MarkdownToConfluence/convert.sh
RUN sed $'s/\r$//' /MarkdownToConfluence/convert_all.sh
RUN sed $'s/\r$//' /MarkdownToConfluence/convert.sh

ENTRYPOINT ["sh", "/MarkdownToConfluence/convert_all.sh"]