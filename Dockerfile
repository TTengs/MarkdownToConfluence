FROM ubuntu:latest

#ARG DOC_PATH

#ENV DOC_PATH=${DOC_PATH}

#RUN apt-get update && apt-get install -y software-properties-common gcc && \
#    add-apt-repository -y ppa:deadsnakes/ppa

#RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt

#RUN apt-get install -y pandoc

COPY src src
COPY dinMor docs/

#RUN chmod +x /src/convert_all.sh
RUN chmod +x /src/entrypoint.sh

ENTRYPOINT ["/src/entrypoint.sh"]