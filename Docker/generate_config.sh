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

oci ce cluster create-kubeconfig --cluster-id "$CLUSTER_OCID" --file $HOME/.kube/config --region "$REGION" --token-version 2.0.0  --kube-endpoint PUBLIC_ENDPOINT
echo "KUBECONFIG SET!"


