# OKE-Connect

A simple python-cli tool to help drive the OKE-Operator-Container.

## Makefile usage

To create the venv, run `make venv` 


To run (build) the program, use `make run`


To clean, do `make clean`

## Using

To use the tool (atleast to see help and test for now - WIP)

1. Run `make venv` to build the virtual env
2. Run `source python39env/bin/activate` to use the venv
3. Run `make run` to build the oke-connect tool
4. Run `oke-connect` or `oke-connect shell` to use the tool with guidance


Source :  https://medium.com/nerd-for-tech/how-to-build-and-distribute-a-cli-tool-with-python-537ae41d9d78


## Config File:

The configuration file is a JSON file that includes mappings from the key to a region name / cluster ocid. This file is then read by the tool and will run a container on request for a certain key

The data structure looks like:

```
    {
	"production-uk-london-1": {
		"region": "uk-london-1",
		"cluster_ocid": "aaaaa"
	},
	"development-uk-london-1": {
		"region": "uk-london-1",
		"cluster_ocid": "bbbb"
	}
}
```
