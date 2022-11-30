import click
import command
import subprocess

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
def shell():
    run_shell()

def run_shell():

    region = "uk-london-1"
    print(f"Killing running oke-operator-tool container for {region} if any")
    subprocess.run(["podman", "container","rm","-f", f"oke-operator-tool-{region}"])
    print("Running oke-operator-tool container with the given cluster and region")
    subprocess.run(["podman","run","-d", "-t", "--name",f"oke-operator-tool-{region}", "--env","CLUSTER_OCID=ocid1.cluster.oc1.uk-london-1.aaaaaaaaao5d3nonea7h7krgyosec7afcstznbptf54scrmfvcomrxfpu3da", "--env", f"REGION={region}", "localhost/operator-tool:latest"])

    print(f"You can now run \"podman attach oke-operator-tool-{region}\" to attach to the running container")


