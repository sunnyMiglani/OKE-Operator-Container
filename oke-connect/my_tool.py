import click

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

