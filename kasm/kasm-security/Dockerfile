# syntax=docker/dockerfile:experimental
ARG IMAGE_TAG=x
ARG BASE_IMAGE="ohmymndy/kasm-ubuntu-base:${IMAGE_TAG}"
FROM $BASE_IMAGE

USER root

RUN apt-get update && deb-get install firefox && apt-get clean

RUN apt-get update && apt-get install -y -q protonmail-bridge protonvpn && apt-get clean

USER kasm-user
