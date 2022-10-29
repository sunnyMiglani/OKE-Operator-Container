build:
	docker build -t operator-tool ./Docker --build-arg CLUSTER_OCID="${CLUSTER_OCID}" --build-arg REGION=${REGION}

build-arm:
	docker build -t operator-tool ./Docker --build-arg CLUSTER_OCID="${CLUSTER_OCID}" --build-arg REGION="${REGION}" --build-arg BUILD_ARCH="arm64v8"

