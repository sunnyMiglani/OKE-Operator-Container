# OKE-Connect

A simple python-cli tool to help drive the OKE-Operator-Container.

WIP:
- Intended to work by commands like `oke-connect uk-london-1` or `oke-connect uk-london-1-dev`. Where we feed in a config file (json) with tthe mappings from `uk-london-1` and `uk-london-1-dev` to different OKE Cluster OCID and region mappings


## Makefile usage

To create the venv, run `make venv` 


To run (build) the program, use `make run`


To clean, do `make clean`

Source :  https://medium.com/nerd-for-tech/how-to-build-and-distribute-a-cli-tool-with-python-537ae41d9d78
