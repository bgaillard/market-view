import click


@click.group
def cli() -> None:
    """Market view CLI."""


@click.command(name="generate-index-assets")
def command_generate_index_assets() -> None:
    """Generates all the assets associated to a specific market index."""
    print("Yes!")


@click.command(name="server")
def command_server() -> None:
    """Start the web server."""
    print("Serve!")


cli.add_command(command_generate_index_assets)

if __name__ == '__main__':
    cli(color=True)
