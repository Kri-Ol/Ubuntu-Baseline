# Docker to build baseline to make other images to run dose calc remotely
FROM ubuntu:16.04
MAINTAINER O.K. <https://github.com/Kri-Ol/Ubuntu-Baseline>

ENV DEBIAN_FRONTEND noninteractive

# commands and configuration
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get autoremove; apt-get autoclean; apt-get clean

RUN apt-get install -y --no-install-recommends python-numpy && \
    apt-get install -y --no-install-recommends python-paramiko && \
    apt-get install -y --no-install-recommends net-tools && \
    apt-get install -y --no-install-recommends sshpass && \
    apt-get install -y --no-install-recommends iputils-ping && \
    apt-get install -y --no-install-recommends xz-utils && \
    apt-get install -y --no-install-recommends wget && \
    apt-get install -y --no-install-recommends wput && \
    apt-get install -y --no-install-recommends nano && \
    apt-get autoremove; apt-get autoclean; apt-get clean

RUN apt-get install -y --no-install-recommends qt4-default && \
    apt-get install -y --no-install-recommends libqt4-opengl && \
    apt-get install -y --no-install-recommends mesa-utils && \
    apt-get install -y --no-install-recommends libxerces-c3.1 && \
    apt-get install -y --no-install-recommends openssh-client && \
    apt-get autoremove; apt-get autoclean; apt-get clean

# make home dir
RUN mkdir -p /home/beamuser

ENV DEBIAN_FRONTEND teletype
ENV PYTHONIOENCODING UTF-8
