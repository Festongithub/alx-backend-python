#!/usr/bin/env python3
"""Async generator"""


import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields a rnadom integer"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
