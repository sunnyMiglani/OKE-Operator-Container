import click
import docker
import command
import subprocess

class DockerTalker:
    def __init__(self):
        self.client = docker.from_env()

@click.group()
def cli():
    pass

@cli.command()
def help():
    click.echo("Please check the readme for help!") # TODO: Give more help

@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}')

@cli.command()
def container():
    setup_docker()

# Docker section - TODO: Cleanup
def setup_docker():
    dockerclient = DockerTalker()
    dockerclient.client.containers.run("ubuntu", "echo hello world")

@cli.command()
def shell():
    run_shell()

def run_shell():
    region = "uk-london-1"
    print("Killing running oke-operator-tool container if any")
    subprocess.run(["podman", "kill", "oke-operator-tool-"+region])

    
    print("Running oke-operator-tool container with the given cluster and region")
    subprocess.run(["podman","run","-d", "-t", "--name","oke-operator-tool-"+region, "--env","CLUSTER_OCID=ocid1.cluster.oc1.uk-london-1.aaaaaaaaao5d3nonea7h7krgyosec7afcstznbptf54scrmfvcomrxfpu3da", "--env", "REGION="+region, "localhost/operator-tool:latest"])

    print("You can now run \"docker attach oke-operator-tool\" to attach to the running container")


