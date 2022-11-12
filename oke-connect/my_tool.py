import click
import docker


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

