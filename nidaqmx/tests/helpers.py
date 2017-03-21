import random
import sys


def generate_random_seed():
    return random.randint(0, sys.maxsize)


def is_close(a, b, rel_tol=1e-09, abs_tol=0.0):
    """
    Determines whether one float value is approximately equal or "close"
    to another float value.

    Copied from PEP 485.

    Args:
        a (float): Specifies the first value to be tested for relative
            closeness.
        b (float): Specifies the second value to be tested for relative
            closeness.
        rel_tol (float): Specifies the relative tolerance -- it is the
            amount of error allowed, relative to the larger absolute
            value of a or b. For example, to set a tolerance of 5%, use
            rel_tol=0.05. The default tolerance is 1e-9, which assures
            that the two values are the same within about 9 decimal
            digits. rel_tol must be greater than 0.0.
        abs_tol (float): Specifies a minimum absolute tolerance level --
            useful for comparisons near zero.

    Returns:
        bool: Indicates whether the first float value is approximately
            equal or "close" to the second float value.
    """
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)