import click
import command
import subprocess

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
@click.option('-r', '--region', type=str, help='Which region to use', required=True)
def shell(region):
    run_shell(region)


def run_shell(region):
    cluster_ocid="ocid1.cluster.oc1.uk-london-1.aaaaaaaaao5d3nonea7h7krgyosec7afcstznbptf54scrmfvcomrxfpu3da"
    if region == "":
        print("Please enter a region")
        return
    print(f"Checking whether a container is running for {region}")
    cmd = f"podman container list -a | grep oke-operator-tool-{region}"
    container_exists = run_cmd(cmd)
    if container_exists:
        print(f"Possibly found container, restarting container")
        cmd = f"podman container restart  oke-operator-tool-{region}"
        restarted_container = run_cmd(cmd)
        if not restarted_container:
            print("ERROR: Unable to restart container, will kill and proceed")
            cmd = f"podman container rm -f oke-operator-tool-{region}"
            container_killed = run_cmd(cmd)
            if not container_killed:
                print("ERROR: Unable to recover, couldn't kill container")
    if not container_exists:
        cmd = f"podman run -d -t --name oke-operator-tool-{region} --env CLUSTER_OCID={cluster_ocid} --env REGION={region} localhost/operator-tool:latest"
        container_started = run_cmd(cmd)
        if not container_started:
            print("ERROR: Unable to start container")
            return
    print(f"You can now run \"podman attach oke-operator-tool-{region}\" to attach to the running container")

def run_cmd(cmd):
    completed_process = subprocess.run(cmd, shell=True)
    if completed_process != None:
        return completed_process.returncode == 0
    else:
        return False
        
