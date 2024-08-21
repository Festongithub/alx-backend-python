#!/usr/bin/env python3

"""Basics of asynchronous"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Float randomness"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
