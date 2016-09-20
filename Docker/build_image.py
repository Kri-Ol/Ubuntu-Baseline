#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import shutil

def main():
    """
    Building Docker image for Ubuntu baseline
    """

    # step last - build docker image
    rc = subprocess.call(["docker", "build", "-t", "ubuntu:baseline",  "."], stderr=subprocess.PIPE)
    if rc != 0:
        raise RuntimeError("Unable to build docker image")

    return rc

if __name__ == '__main__':
    sys.exit(main())
