from functools import reduce
from operator import add, mul
from itertools import repeat
from math import ceil
from typing import List, Tuple, TypeVar, Generic
from typing import Tuple, TypeVar, Callable

T = TypeVar('T')

class Iso(Generic[T]):
    def __init__(self, to_fun, from_fun):
        self.to = to_fun
        self.from_ = from_fun

# This function encodes a list of values using an isomorphism
def encode(iso: Iso[Tuple[T, int], int], lst: List[T]) -> int:
    # Reduce function is used to apply the to function of the given isomorphism to each element of the input list
    # The initial accumulator value is set to 1
    return reduce(lambda acc, s: iso.to((s, acc)), lst, 1)

# # This function encodes a list of values using an isomorphism
# def encode(iso: Iso[Tuple[T, int], int]) -> int:
#     # Reduce function is used to apply the to function of the given isomorphism to each element of the input list
#     # The initial accumulator value is set to 1
#     return reduce(lambda acc, s: iso.to((s, acc)), 1)


# This function encodes a list of values using an isomorphism
def encode(iso: Iso[Tuple[T, int]]) -> int:
    # Reduce function is used to apply the to function of the given isomorphism to each element of the input list
    # The initial accumulator value is set to 1
    return reduce(lambda acc, s: iso.to((s, acc)), 1)


# # This function decodes an integer to a list of values using the given isomorphism
# def decode(iso: Iso[Tuple[T, int], int], n: int) -> List[T]:
#     res = []
#     # Repeatedly apply the from_ function of the given isomorphism to the input integer until we reach the base value
#     while n != 1:
#         s, n = iso.from_(n)
#         res.append(s)
#     # Return the resulting list in reverse order
#     return res[::-1]


# This function decodes an integer to a list of values using the given isomorphism
def decode(iso: Iso[Tuple[T, int]]) -> List[T]:
    res = []
    # Repeatedly apply the from_ function of the given isomorphism to the input integer until we reach the base value
    while n != 1:
        s, n = iso.from_(n)
        res.append(s)
    # Return the resulting list in reverse order
    return res[::-1]


# This function converts a value to an integer using the __index__ method
def s2n(s: T) -> int:
    return (s.__index__() -
            type(s).__dict__.get("min", 0).__index__())

# This function converts an integer to a value using the given class type
def n2s(n: int, s_cls) -> T:
    return s_cls((n + type(s_cls).__dict__.get("min", 0).__index__()))

# This function returns the number of values in the given class type
def base(s_cls) -> int:
    return s2n(s_cls.max) + 1

# # This function returns an isomorphism that maps between tuples of values and integers
# # using the standard encoding scheme
# def std_iso(s_cls) -> Iso[Tuple[T, int], int]:
#     base_ = base(s_cls)

#     def to(s, n):
#         return s2n(s) + base_ * n

#     def from_(n):
#         return (n2s(n % base_, s_cls), n // base_)

#     return Iso(to, from_)


# This function returns an isomorphism that maps between tuples of values and integers
# using the standard encoding scheme
def std_iso(s_cls) -> Iso[Tuple[T, int]]:
    base_ = base(s_cls)

    def to(s, n):
        return s2n(s) + base_ * n

    def from_(n):
        return (n2s(n % base_, s_cls), n // base_)

    return Iso(to, from_)


# from typing import Tuple, TypeVar
# from iso import Iso

T = TypeVar('T')

def ans_iso(s_cls, classify):
    # Get the base and the classification function from the `classify` tuple
    b, cls = classify

    def to(s, n):
        """Convert a tuple of a value and an integer to an integer."""
        # Create a list of integers that have the same value as `s`
        l = [k for k in range(b, b + n * b) if cls(k) == s]
        # Return the last integer in the list
        return l[-1]

    def from_(n):
        """Convert an integer to a tuple of a value and an integer."""
        # Get the value of the integer using the classification function
        s = cls(n)
        # Create a list of integers that have the same value as `s`
        l = [k for k in range(b, b + (n + 1) * b) if cls(k) == s]
        # Get the index of the integer in the list and subtract `b` to get the integer's index within its block
        n_ = l.index(n + b)
        # Return a tuple of the value and the integer's index
        return (s, n_)

    # Return an isomorphism object that maps between tuples of a value and an integer and integers
    return Iso(to, from_)

def classify_mod_base(s_cls) -> Tuple[int,  Callable[[T], int]]:
    """Classifies characters based on modular arithmetic with the base of the character set."""
    # Compute the base of the character set
    base_ = base(s_cls)

    def classify(n: int) -> T:
        """Given a number `n`, return the corresponding character in the character set `s_cls`."""
        return n2s(n % base_, s_cls)

    return (base_, classify)

def classify_prob(s_cls, probs: List[float]) -> Tuple[int, Callable[[int], T]]:
    """Classifies characters based on a list of probabilities."""
    t = len(probs)
    # Repeat each character in the character set `s_cls` based on its probability value
    l = [s for i, s in enumerate(s_cls) for _ in range(round(probs[i] / min(probs)))]
    
    def g1(n):
        """Given a number `n`, return the corresponding character in the character set `s_cls`."""
        return l[(n - 2) % len(l)]
    
    return (2, g1)

def test_encode_decode() -> None:
    """Tests the `encode` and `decode` functions for boolean values."""
    iso = std_iso(bool)
    assert decode(iso, encode(iso, [])) == []
    assert decode(iso, encode(iso, [True])) == [True]
    assert decode(iso, encode(iso, [False])) == [False]
    assert decode(iso, encode(iso, [True, False, True])) == [True, False, True]

def test_encode_decode_ans_iso() -> None:
    """Tests the `encode` and `decode` functions for boolean values using the `ans_iso` function."""
    iso = ans_iso(bool, classify_mod_base(bool))
    assert decode(iso, encode(iso, [])) == []
    assert decode(iso, encode(iso, [True])) == [True]