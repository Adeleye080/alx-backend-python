#!/usr/bin/env python3
import asyncio
from typing import Generator
import random
""" Async Generator. """


async def async_generator() -> Generator:
    """ Generates 10 random number. """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
