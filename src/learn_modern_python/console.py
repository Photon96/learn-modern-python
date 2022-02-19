import textwrap

import click
import requests

from . import __version__

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

@click.command()
@click.version_option(version = __version__)
def main():
    """The modern Python project"""

    with requests.get(API_URL) as response:
        status_code = response.status_code
        if (status_code != requests.codes.ok):
            click.secho(f"Bad request {status_code}", fg="red")
            return
        data = response.json()
    
    title = data['title']
    extract = data['extract']

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))