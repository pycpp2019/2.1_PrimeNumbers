from sympy import primerange
from prime import primes


def test_0():
    assert len(primes(0)) == 0

def test_1():
    pl = primes(3)
    assert len(pl) == 1
    assert pl[0] == 2

def _test_n(n):
    pl = primes(n)
    rpl = list(primerange(2, n))
    assert len(pl) == len(rpl)
    assert all([a == b for a, b in zip(pl, rpl)])

def test_100():
    _test_n(100)

def test_1e4():
    _test_n(10**4)

def test_1e7():
    _test_n(10**7)
