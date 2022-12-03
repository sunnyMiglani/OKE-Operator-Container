#!/bin/bash


# Setup KUBECONFIG
if [[ -z "${CLUSTER_OCID}" ]]; then
    echo "CLUSTER_OCID NOT SET!"
    exit 1
fi
if [[ -z "${REGION}" ]]; then
    echo "REGION NOT SET!"
    exit 1
fi

echo "Connecting to ${CLUSTER_OCID} in ${REGION}"

oci ce cluster create-kubeconfig --cluster-id "$CLUSTER_OCID" --file $HOME/.kube/config --region "$REGION" --token-version 2.0.0  --kube-endpoint PUBLIC_ENDPOINT
if [[ $? -eq 0 ]] ; then
    echo "KUBECONFIG successfully set!"
else 
    echo "Failed to set KUBECONFIG"
fi


