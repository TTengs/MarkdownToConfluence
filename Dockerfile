FROM ubuntu:latest

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt

RUN apt-get install -y pandoc

COPY src ${GITHUB_WORKDIR}/scripts
COPY dinMor ${GITHUB_WORKDIR}/docs

RUN ls
#${INPUT_DOCS_PATH}
RUN chmod +x ${GITHUB_WORKDIR}/scripts/convert_all.sh
RUN chmod +x ${GITHUB_WORKDIR}/scripts/entrypoint.sh

#Entrypoint kører scripts på workflowet og ikke containerne==!=!?!?!??
ENTRYPOINT ["${GITHUB_WORKDIR}/scripts/entrypoint.sh"]