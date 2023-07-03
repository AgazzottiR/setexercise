"""This module contains helper functions to check  computed results.
"""
from collections.abc import Iterable

def result_verifier(a,b):
    """ Checks Results. converts subsets in tuple to become hashable types
        and checks the equalities for the sets.

    Args:
        a (iterable[iterable[int]) 
        b (iterable[iterable[int])

    Returns:
        boolean: True if sets are equal, false otherwise
    """
    
    a = [tuple(sorted(val)) for val in a]
    a = set(a)
    b = [tuple(sorted(val)) for val in b]
    b = set(b)

    return a == b    