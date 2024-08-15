#!/usr/bin/env python3
"""Duck types"""

from typing import Mapping, MutableMapping, Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns elements Length"""
    return [(i, len(i)) for i in lst]
