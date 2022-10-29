#!/bin/bash

# Setup KUBECONFIG
if [[ -z "${CLUSTER_OCID}" ]]; then
    echo "CLUSTER_OCID NOT SET!"
    exit 1
fi
oci ce cluster create-kubeconfig --cluster-id "$CLUSTER_OCID" --file $HOME/.kube/config --region uk-london-1 --token-version 2.0.0  --kube-endpoint PUBLIC_ENDPOINT
echo "KUBECONFIG SET!"


