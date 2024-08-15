#!/usr/bin/env python3
""" Duck typing - first element of a sequence"""
from typing import Any, Callable, Iterable, Mapping,
MutableMapping, List, Sequence, Tuple


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Sequence of a list"""
    if lst:
        return lst[0]
    else:
        return None
