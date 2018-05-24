# -*- coding: utf-8 -*-
"""
Created on Wed May 23 13:29:10 2018

@author: prabhudayala
"""

"""Miscellaneous utility functions."""

from functools import reduce


def compose(*funcs):
    """Compose arbitrarily many functions, evaluated left to right.

    Reference: https://mathieularose.com/function-composition-in-python/
    """
    # return lambda x: reduce(lambda v, f: f(v), funcs, x)
    if funcs:
        return reduce(lambda f, g: lambda *a, **kw: g(f(*a, **kw)), funcs)
    else:
        raise ValueError('Composition of empty sequence not supported.')
