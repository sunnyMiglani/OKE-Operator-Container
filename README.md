# Operator Tool

This operator tool (better name tbd) is used to help extract and use a kubeconfig for a particular OKE cluster in Oracle Cloud Infrastructure

## oke-connect tool

The oke-connect tool will help drive the creation and running of the containers
At this point it's only supporting a hardcoded cluster-ocid, but this will be fixed

## Setup

1. Copy / Setup a `.oci` folder in the `Docker` directory of this project (this folder is .gitignored)
2. Run `make` to build the dockerfile
3. To run the container do `docker run --env REGION="region-name-here" --env CLUSTER_OCID="ocid1.cluster.ocid.here" -it localhost/operator-tool:latest` 

Inside the container you should now have oci-cli installed and your configuration copied into the container, this will let you run specific OCI CLI commands


## Current Limitations:

### OCI Config file setup

The OCI config file requires a path to the private key associated with the relevant user. A limitation of this tool currently is that the `path` var should be relative to `~` to ensure the kubeconfig setup script works correctly.

Without this step, OCI CLI commands will not work

e.g You must have a config path that looks like:

```
user=ocid1.user.oc1..aaa.... user here
fingerprint=fi:ng:er:pr:in:nt:he:re
tenancy=ocid1.tenancy.oc1...aaaaa tenancy id here
region=uk-london-1
key_file=~/.oci/oci_api_key.pem # See relative path from ~
compartment-id=ocid1.tenancy......compartment here
```

### oke-connect only supports Podman

At the moment, oke-connect hardcodes podman commands into the shell commands. 
