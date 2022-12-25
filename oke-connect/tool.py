import click
import command
import subprocess
import json


CONFIG_FILE = "oke-connect.json"

@click.group()
def cli():
    pass

# This command clears existing containers, if given a config file, will kill containers only present in the config file
@cli.command(short_help='cleanup containers')
@click.option('-f','--config-file', type=click.Path(exists=True, dir_okay=False),help='Path to the config file', required=True)
def cleanup(config_file=None):
    """
        This command will cleanup the existing containers based on the given configuration file.
    """
    global CONFIG_FILE
    if config_file != None:
        print(config_file)
        CONFIG_FILE=config_file
    cleanupContainers(config_file)


@cli.command(short_help='create and run a container')
@click.option('-c', '--cluster-id', type=str, help='Which cluster to use', required=True)
@click.option('-f','--config-file', type=click.Path(exists=True, dir_okay=False),help='Path to the config file', required=False)
@click.option('--force-init', type=bool, help='Whether to force initialization of a new container', required=False)
def shell(cluster_id, config_file=None, force_init=False):
    """
        This command will run a contianer for a given cluster_id based on data provided in a configuration file.
    """
    # We want to use the global version of this variable
    global CONFIG_FILE
    if config_file != None:
        print(config_file)
        CONFIG_FILE=config_file
        print(CONFIG_FILE)
    runShell(CONFIG_FILE,cluster_id, force_init)

def cleanupContainers(config_file):
    keys_list = getConfigKeysFromFile(config_file)
    if keys_list == []:
        print("No keys found from config file!")
    for key in keys_list:
        print(f"Checking whether container for {key} exists")
        container_exists = findContainer(key)
        if container_exists:
            print(f"Removing container for {key}")
            removed_container = removeContainer(key)
            if not removed_container:
                print(f"Error removing container for {key}")

def getConfigKeysFromFile(config_file):
    f = open(CONFIG_FILE, "r")
    data = json.load(f)
    if data != None:
        return data.keys()
    else: 
        return []
def getClusterDataFromConfig(config_file, key):
    f = open(CONFIG_FILE, "r")
    data = json.load(f)
    region = ""
    cluster_id = ""

    if key in data:
        region = data[key]["region"]
        cluster_id = data[key]["cluster_ocid"]
    else:
        raise click.ClickException(f"Required key {key} not found in config file")

    return region, cluster_id

def findContainer(config_key):
    cmd = f"podman container list -a | grep oke-operator-tool-{config_key}"
    container_exists = runCommand(cmd)
    return container_exists

def restartContainer(config_key):
    cmd = f"podman container restart oke-operator-tool-{config_key}"
    restarted_container = runCommand(cmd)
    return restarted_container

def removeContainer(config_key):
    cmd = f"podman container rm -f oke-operator-tool-{config_key}"
    container_killed = runCommand(cmd)
    return container_killed

def runContainer(config_key, cluster_ocid, region):
    cmd = f"podman run -d -t --name oke-operator-tool-{config_key} --env CLUSTER_OCID={cluster_ocid} --env REGION={region} localhost/operator-tool:latest"
    container_started = runCommand(cmd)
    return container_started

def runShell(config_file,config_key, force_init):
    print(f"Reading cluster data from config file for {config_key}")
    region, cluster_ocid = getClusterDataFromConfig(config_file, config_key)

    print(f"Checking whether a container is running for {config_key}")
    container_exists = findContainer(config_key)
    if force_init:
        if container_exists:
            print(f"Killing container as force init requested")
            container_killed = removeContainer(config_key)
            if not container_killed:
                print("Unrecoverable error: Unable to kill container, cannot proceed")
                return
    elif container_exists:
        print(f"Possibly found container")
        print(f"Restarting container")
        restarted_container = restartContainer(config_key)
        if not restarted_container:
            print("ERROR: Unable to restart container, will kill and proceed")
            container_killed = removeContainer(config_key)
            if not container_killed:
                print("ERROR: Unable to recover, couldn't kill container")
                return
    if not container_exists or force_init:
        print(f"Starting container for {config_key}")
        container_started = runContainer(config_key, cluster_ocid, region)
        if not container_started:
            print("ERROR: Unable to start container")
            return
    print(f"You can now run \"podman attach oke-operator-tool-{config_key}\" to attach to the running container")

def runCommand(cmd):
    completed_process = subprocess.run(cmd, shell=True)
    if completed_process != None:
        return completed_process.returncode == 0
    else:
        return False
        
