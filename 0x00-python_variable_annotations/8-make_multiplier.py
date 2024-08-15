#!/usr/bin/env python3

"""Functions"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns float multiplier"""
    def multiplier_function(n: float) -> float:
        """Flaot"""
        return n * multiplier
    return multiplier_function
