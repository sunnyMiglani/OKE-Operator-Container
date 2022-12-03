import click
import command
import subprocess
import json


CONFIG_FILE = "oke-connect.json"

@click.group()
def cli():
    pass

@cli.command()
def help():
    click.echo("Please check the readme for helpnot ") # TODO: Give more help

@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}')

@cli.command()
@click.option('-c', '--cluster-id', type=str, help='Which cluster to use', required=True)
@click.option('-f','--config-file', type=click.Path(exists=True, dir_okay=False),help='Path to the config file', required=False)
def shell(cluster_id, config_file=None):
    # We want to use the global version of this variable
    global CONFIG_FILE
    if config_file != None:
        print(config_file)
        CONFIG_FILE=config_file
        print(CONFIG_FILE)
    runShell(CONFIG_FILE,cluster_id)


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


def runShell(config_file,config_key):
    print(f"Reading cluster data from config file for {config_key}")
    region, cluster_ocid = getClusterDataFromConfig(config_file, config_key)
    print(f"Checking whether a container is running for {config_key}")
    cmd = f"podman container list -a | grep oke-operator-tool-{config_key}"
    container_exists = run_cmd(cmd)
    if container_exists:
        print(f"Possibly found container, restarting container")
        cmd = f"podman container restart  oke-operator-tool-{config_key}"
        restarted_container = run_cmd(cmd)
        if not restarted_container:
            print("ERROR: Unable to restart container, will kill and proceed")
            cmd = f"podman container rm -f oke-operator-tool-{config_key}"
            container_killed = run_cmd(cmd)
            if not container_killed:
                print("ERROR: Unable to recover, couldn't kill container")
    if not container_exists:
        cmd = f"podman run -d -t --name oke-operator-tool-{config_key} --env CLUSTER_OCID={cluster_ocid} --env REGION={region} localhost/operator-tool:latest"
        container_started = run_cmd(cmd)
        if not container_started:
            print("ERROR: Unable to start container")
            return
    print(f"You can now run \"podman attach oke-operator-tool-{config_key}\" to attach to the running container")

def run_cmd(cmd):
    completed_process = subprocess.run(cmd, shell=True)
    if completed_process != None:
        return completed_process.returncode == 0
    else:
        return False
        
