import re
from sympy import primerange


def test_prime():
    with open("prime.txt", "r") as f:
        pl = [int(s) for s in re.sub(r"[^0-9]+", " ", f.read()).strip().split(" ")]
    rpl = list(primerange(2, 10**7))
    assert len(pl) == len(rpl)
    assert all([a == b for a, b in zip(pl, rpl)])
