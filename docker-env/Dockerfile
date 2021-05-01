# Download base image ubuntu 20.04
FROM ubuntu:20.04

# LABELs
LABEL maintainer="dmpeletronic@gmail.com"
LABEL version="0.1"
LABEL description="This is a custom ubuntu for oplab Test environment"

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# Update packages
RUN apt update

# Install: gcc/g++ python Erlang
RUN apt install -y build-essential 
RUN apt install -y python3