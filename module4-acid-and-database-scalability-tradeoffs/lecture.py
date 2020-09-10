#!/usr/bin/env python
import itertools
import operator
from collections import Iterable, Callable
from itertools import product


def transform_reduce(lhs: Iterable, rhs: Iterable,
                     transformer: Callable, reducer: Callable):
    """ Transform Reduce
    Pairwise transform and then reduction across all results.
    DocTests:
    >>> transform_reduce(range(1, 6), range(1, 6), operator.mul, sum)
    55
    >>> transform_reduce(range(1, 6), range(1, 6), operator.add, product)
    3840
    @param lhs: Left Iterator
    @param rhs: Right Iterator
    @param transformer: Binary Functor F(x, y) -> Value
    @param reducer: Reduction Functor F(Iterable) -> Value
    @return: Reduced Value
    """
    return reducer(itertools.starmap(transformer, zip(lhs, rhs)))


def inner_product(lhs: Iterable, rhs: Iterable):
    """ Inner Product
    Performs pairwise multiplication across the iterables,
        then returns the sum of the products.
    DocTests:
    >>> inner_product(range(1, 6), range(1, 6))
    55
    >>> inner_product(range(11), range(11))
    385
    @param lhs: Left Iterator
    @param rhs: Right Iterator
    @return: Sum of the products.
    """
    return transform_reduce(lhs, rhs, operator.mul, sum)