#!/usr/bin/env python
import click
import requests
import json
from adventure import Adventure

@click.command()
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)


def doStep(step):
    ad = Adventure('data.json')
    click.clear()
    click.echo(click.style(ad.title(step), bold=True))
    click.echo(click.style(ad.text(step)))

    if ad.choices(step) is None:
        click.echo(click.style('End of your journey goodbye.', fg='red'))
        quit()

    for option in ad.choices(step):
        click.echo(click.style('['+str(option['id'])+'] ' + option['text']))

    choice = click.prompt('What do you want to do ?', type = int)
    doStep(ad.choices(step)[choice-1]['link'])

if __name__ == '__main__':
    doStep(1)