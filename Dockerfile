# syntax=docker/dockerfile:1

FROM ubuntu:latest
RUN apt update
RUN apt install -y git
RUN cd home
RUN 