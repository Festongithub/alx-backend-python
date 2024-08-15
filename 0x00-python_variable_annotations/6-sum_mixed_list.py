#!/usr/bin/env python3
"""Mixed lists"""

from typing import Callable, Iterator, Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of floats"""
    return float(sum(mxd_lst))
