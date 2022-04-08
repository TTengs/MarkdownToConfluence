FROM ubuntu:latest

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt

RUN apt-get install -y pandoc

COPY src /scripts
COPY ${INPUT_DOCS_PATH} /docs

RUN echo "${INPUT_DOCS_PATH}"
#${INPUT_DOCS_PATH}
RUN chmod +x /scripts/convert_all.sh
RUN chmod +x /scripts/entrypoint.sh

#Entrypoint kører scripts på workflowet og ikke containerne==!=!?!?!??
ENTRYPOINT ["/scripts/entrypoint.sh"]