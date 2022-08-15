import click

from click import Context

from marketview.api import start as start_server
from marketview.assets_generator import generate_for_company


@click.group
def cli() -> None:
    """Market view CLI."""


@click.command(name="generate-assets")
@click.option(
    "--ticker",
    default="AI.PA",
    show_default=True,
    required=True,
    help="The ticker associated to the company for which one to generate assets."
)
@click.pass_context
def command_generate_assets(context: Context, ticker: str) -> None:
    """Generates all the assets for a specific company."""
    generate_for_company(ticker=ticker, period="50y")


@click.command(name="serve")
def command_serve() -> None:
    """Start the web server."""
    start_server()


cli.add_command(command_generate_assets)
cli.add_command(command_serve)

if __name__ == '__main__':
    cli(color=True)
