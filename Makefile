build:
	docker build -t operator-tool ./Docker --build-arg CLUSTER_OCID="${CLUSTER_OCID}" --build-arg REGION=${REGION}

