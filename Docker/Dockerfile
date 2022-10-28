FROM oraclelinux:8

ARG CLUSTER_OCID
ARG REGION

RUN dnf -y install oraclelinux-developer-release-el8
RUN dnf install -y python36-oci-cli

COPY .oci/* /.oci/
COPY ./generate_config.sh /root/
CMD chmod +x /root/generate_config.sh

ENV CLUSTER_OCID=$CLUSTER_OCID
ENV REGION=$REGION
