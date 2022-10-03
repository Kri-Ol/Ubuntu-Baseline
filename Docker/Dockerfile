# Docker to build baseline to make other images to run dose calc remotely
FROM ubuntu:18.04
MAINTAINER O.K. <https://github.com/Kri-Ol/Ubuntu-Baseline>

ENV DEBIAN_FRONTEND noninteractive

# commands and configuration
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get install -y --no-install-recommends wget && \
    apt-get autoremove; apt-get autoclean; apt-get clean

RUN apt-get install -y --no-install-recommends python3.7 && \
    apt-get install -y --no-install-recommends python3.7-venv && \
    apt-get install -y --no-install-recommends python3-distutils && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1

RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3.7 get-pip.py && \
    rm get-pip.py && \
    pip install numpy && \
    pip install paramiko

RUN apt-get install -y --no-install-recommends net-tools && \
    apt-get install -y --no-install-recommends sshpass && \
    apt-get install -y --no-install-recommends iputils-ping && \
    apt-get install -y --no-install-recommends xz-utils && \
    apt-get install -y --no-install-recommends wput && \
    apt-get install -y --no-install-recommends nano && \
    apt-get install -y --no-install-recommends libgfortran3 && \
    apt-get autoremove; apt-get autoclean; apt-get clean

RUN pip install google-cloud-storage

# make home dir
RUN mkdir -p /home/beamuser

ENV DEBIAN_FRONTEND teletype
ENV PYTHONIOENCODING UTF-8
