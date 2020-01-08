"""Implements default stdout-like functions. """

import click

COLOR_SCHEMA = {
    "ok": {
        "fg": "green"
    },
    "warn": {
        "fg": "yellow"
    },
    "error": {
        "fg": "red"
    },
    "info": {
        "fg": "blue"
    }
}


def _colored_ok(msg):
    """
    Colored success output function.
    """
    msg = str(msg)
    click.secho(msg, **COLOR_SCHEMA['ok'])


def _colored_warn(msg):
    """
    Colored warning output function.
    """
    msg = str(msg)
    click.secho(msg, **COLOR_SCHEMA['warn'])


def _colored_error(msg):
    """
    Colored errors output function.
    """
    msg = str(msg)
    click.secho(msg, **COLOR_SCHEMA['error'])


def _colored_info(msg):
    """
    Colored info output function.
    """
    msg = str(msg)
    click.secho(msg, **COLOR_SCHEMA['info'])


ok = _colored_ok
warn = _colored_warn
error = _colored_error
info = _colored_info
out = click.echo

