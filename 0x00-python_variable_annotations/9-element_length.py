#!/usr/bin/env python3
from typing import List, Callable, Mapping, MutableMapping, Sequence, Iterable

"""Duck Type an iterable object """


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns elements Length"""
    return [(i, len(i)) for i in lst]
