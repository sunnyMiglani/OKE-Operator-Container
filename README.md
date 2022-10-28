# Operator Tool

This operator tool (better name tbd) is used to help extract and use a kubeconfig for a particular OKE cluster in Oracle Cloud Infrastructure

## Setup

1. Copy / Setup a `.oci` folder in the root directory of this project (this folder is .gitignored)
2. Run docker build -t operator-tool . 
3. Run docker exec -it operator-tool 

Inside the container you should now have oci-cli installed and your configuration copied into the container, this will let you run specific OCI CLI commands

## TODO:

- [ ] Setup `$CLUSTER_OCID` and `$REGION` environment variables to pickup kubeconfig
- [ ] Add "get kubeconfig" logic into a startup script based on these environment variables
- [ ] ... and more


