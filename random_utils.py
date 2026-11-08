import random


def random_integer_pair(upper):
    """Return a pair of distinct random integers in [0, upper)."""
    a = random.randrange(upper)
    r = random.randrange(upper - 1)
    b = (r + a + 1) % upper
    return a, b


def random_sorted_integer_pair(upper):
    """Same as random_integer_pair, but the pair is returned in increasing order."""
    a, b = random_integer_pair(upper)
    return (a, b) if a < b else (b, a)


def random_uniform():
    """Random sample from the uniform distribution on [0, 1)."""
    return random.random()
