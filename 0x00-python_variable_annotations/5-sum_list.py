#!/usr/bin/env python3

from typing import List

"""Takes sum of list"""


def sum_list(input_list: List[float]) -> float:
    """takes list input_list of flaots as arguments
    and returns their sum as a float
    """
    return sum(float(input_list))
