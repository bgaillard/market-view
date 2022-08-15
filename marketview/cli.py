import click

from marketview.api import start as start_server


@click.group
def cli() -> None:
    """Market view CLI."""


@click.command(name="generate-assets")
def command_generate_assets() -> None:
    """Generates all the assets company."""
    print("Yes!")


@click.command(name="serve")
def command_serve() -> None:
    """Start the web server."""
    start_server()


cli.add_command(command_generate_assets)
cli.add_command(command_serve)

if __name__ == '__main__':
    cli(color=True)
