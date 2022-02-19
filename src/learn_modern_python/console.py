import textwrap
import locale

import click
import requests

from . import __version__

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"

@click.command()
@click.version_option(version = __version__)
@click.option('--language', help="Language version of Wikipedia. Default is your locale")
def main(language):
    """The modern Python project"""
    if language is None:
        local = locale.getlocale()
        language = (local[0])[0:local[0].index("_")]
    with requests.get(API_URL.format(language = language)) as response:
        status_code = response.status_code
        if (status_code != requests.codes.ok):
            click.secho(f"Bad request {status_code}", fg="red")
            return
        data = response.json()
    
    title = data['title']
    extract = data['extract']

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))