# Docker to build baseline to make other images to run dose calc remotely
FROM ubuntu:15.04
MAINTAINER O.K. <https://github.com/Kri-Ol/Ubuntu-Baseline>

# commands and configuration
RUN apt-get update && \
    apt-get install -y python-numpy && \
    apt-get install -y python-paramiko && \
    apt-get install -y net-tools && \
    apt-get install -y sshpass && \
    apt-get install -y iputils-ping && \
    apt-get install -y xz-utils && \
    apt-get install -y wget && \
    apt-get install -y wput && \
    apt-get autoremove; apt-get clean; apt-get autoclean

# make home dir
RUN mkdir -p /home/beamuser
