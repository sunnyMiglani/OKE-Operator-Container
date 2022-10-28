# Operator Tool

This operator tool (better name tbd) is used to help extract and use a kubeconfig for a particular OKE cluster in Oracle Cloud Infrastructure

## Setup

1. Copy / Setup a `.oci` folder in the `Docker` directory of this project (this folder is .gitignored)
2. Run `make` to build the dockerfile
3. Run docker exec -it localhost/operator-tool:latest 

Inside the container you should now have oci-cli installed and your configuration copied into the container, this will let you run specific OCI CLI commands

## TODO:

- [ ] Setup `$CLUSTER_OCID` and `$REGION` environment variables to pickup kubeconfig
- [ ] Add "get kubeconfig" logic into a startup script based on these environment variables
- [ ] ... and more

## Current Limitations:

### OCI Config file setup

The OCI config file requires a path to the private key associated with the relevant user. A limitation of this tool currently is that the `path` var should be relative to `~` to ensure the generate_config script works correctly.

e.g You must have a config path that looks like:

```
user=ocid1.user.oc1..aaa.... user here
fingerprint=fi:ng:er:pr:in:nt:he:re
tenancy=ocid1.tenancy.oc1...aaaaa tenancy id here
region=uk-london-1
key_file=~/.oci/oci_api_key.pem # See relative path from ~
compartment-id=ocid1.tenancy......compartment here
```
