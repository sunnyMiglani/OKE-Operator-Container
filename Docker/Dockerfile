ARG BUILD_ARCH=amd64
FROM docker.io/${BUILD_ARCH}/oraclelinux:8
ARG BUILD_ARCH

# Install oci-cli
RUN dnf -y install oraclelinux-developer-release-el8
RUN dnf install -y python36-oci-cli

ENV BUILD_ARCH=${BUILD_ARCH}

# Install kubectl
## Little bit messy because the arch has different names in kubectl and docker/oraclelinux
# amd64 support
RUN if [[ "$BUILD_ARCH" == "amd64" ]] ; then curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl ; fi

# arm support
RUN if [[ "$BUILD_ARCH" == "arm64v8" ]] ; then curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/arm64/kubectl ; fi

RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin

COPY .oci/* /root/.oci/
COPY ./generate_config.sh /root/
RUN chmod +x /root/generate_config.sh

# Finally, run the generate config step so we can do that as we start
# CMD ["./root/generate_config.sh", ";", "/bin/bash"]
CMD /bin/bash -c './root/generate_config.sh; /bin/bash'
