#!/usr/bin/env python3
# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
from __future__ import annotations

import asyncio
import click
import contextlib
import json
import logging
import os

from logging.handlers import RotatingFileHandler

from src.app import App


# -----------------------------------------------------------
#                          Logger
# -----------------------------------------------------------
@contextlib.contextmanager
def setup_logger():
    """Setup Logger as a Context Manager"""
    try:
        # __enter__
        max_bytes: int = 64 * 1024 * 1024

        logger: logging.Logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        handler: RotatingFileHandler = RotatingFileHandler(
            filename='.logs/fvtt-converter.log', encoding='utf_8', mode='w', maxBytes=max_bytes, backupCount=10)
        date_format = '%Y-%m-%d %H:%M:%S'
        format: logging.Formatter = logging.Formatter(
            '[{asctime}] [{levelname:<7}] {name}: {message}', date_format, style='{')
        handler.setFormatter(format)
        logger.addHandler(handler)

        yield

    finally:
        # __exit__
        handlers = logger.handlers[:]
        for handler in handlers:
            handler.close()
            logger.removeHandler(handler)


# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
# -----------------------------------------------------------
#                          App
# -----------------------------------------------------------
async def run_app():
    """ App Start """
    app = App()
    await app.start()


# -----------------------------------------------------------
#                          Main
# -----------------------------------------------------------
@click.group(invoke_without_command=True, options_metavar='[options]')
@click.pass_context
def main(ctx: click.Context):
    """Starts the process of launching the converter."""
    if ctx.invoked_subcommand is None:
        with setup_logger():
            asyncio.run(run_app())


# -----------------------------------------------------------
#                          Init
# -----------------------------------------------------------
if __name__ == '__main__':
    main()
