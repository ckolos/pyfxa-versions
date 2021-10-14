#!/usr/bin/env python3

""" fxa-release-status re-written in python """

import click
import json
import requests
import pkg_resources


from sys import exit


def die(msg):
    """
    Print a message and exit with 1 status code.
    """
    click.echo(click.style(msg, fg="red"))
    exit(1)


def read_config(config_file):
    """
    read config
    """
    try:
        with open(config_file) as config:
            conf = json.load(config)
            config.close()
            return conf
    except (IOError, ValueError) as e:
        die(f"Error reading config file {config_file} : {e}")


def get_info(site):
    """
    Hit the /__version__ endpoint and return result
    """
    this_site = f"https://{site}/__version__"
    try:
        info = requests.get(this_site)
    except requests.ConnectionError as exc:
        raise click.ClickException(f"Unable to connect to {site}: {exc}")
    except requests.HTTPError as exc:
        raise click.ClickException(f"HTTPError: {exc}")
    except requests.Timeout as exc:
        raise click.ClickException(f"Timeout: {exc}")
    except requests.TooManyRedirects as exc:
        raise click.ClickException(f"Too many redirects encountered: {exc}")

    if info.status_code == 200:
        return info.json
    else:
        die(f"response from {this_site} != 200!")


@click.command()
@click.option(
    "-c",
    "--config",
    default=f'{pkg_resources.resource_filename(__name__, "data/pyfxa-versions.json")}',
    help="The full path to the script's config file",
    required=False,
)
@click.option(
    "-e", "--env", default="stage", help="The env to be checked", required=False
)
def main(config, env):
    """
    main processing
    """
    sites = {}
    config = read_config(config)
    try:
        for site in config[f"{env}"]:
            sites[f"{site}"] = get_info(site)
    except ValueError:
        die(f"Site {site} doesn't exist in {config}")

    for k, v in sites.items():
        print(f"https://{k}/__version__\n{json.dumps(v(), indent=2, sort_keys=True)}\n")


if __name__ == "__main__":
    main()
