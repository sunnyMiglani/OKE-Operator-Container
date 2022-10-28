FROM docker.io/arm64v8/oraclelinux:8
# Install oci-cli
RUN dnf -y install oraclelinux-developer-release-el8
RUN dnf install -y python36-oci-cli

# Install kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/arm64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin

ARG CLUSTER_OCID
ARG REGION

COPY .oci/* /root/.oci/
COPY ./generate_config.sh /root/
RUN chmod +x /root/generate_config.sh

RUN ./root/generate_config.sh

ENV CLUSTER_OCID=$CLUSTER_OCID
ENV REGION=$REGION
