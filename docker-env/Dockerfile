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

# Install: gcc/g++ python cmake Erlang
RUN apt install -y build-essential 
RUN apt install -y python3
RUN apt install -y cmake
RUN apt install -y git

#RUN apt install -y erlang
#Gtest specific build
RUN apt install -y libgtest-dev
COPY build_gtest.sh /opt/
RUN /opt/build_gtest.sh