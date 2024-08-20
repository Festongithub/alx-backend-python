#!/usr/bin/env python3
import asyncio
import random

"""The modules tasks on Async generator"""


async def async_generator():
    """Yields a rnadom integer"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
