from solution import is_prime
from random import randint
import pytest


def check(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def get_param(b):
    if b:
        val = randint(10**5, 10**8)
    else:
        val = randint(-10, 10)
    return val, check(val)


class TestGenerated:

    @pytest.mark.parametrize("value, output", [get_param(False) for _ in range(3)])
    def test_A(self, value, output):
        assert is_prime(value) == output

    @pytest.mark.parametrize("value, output", [get_param(True) for _ in range(3)])
    def test_B(self, value, output):
        assert is_prime(value) == output


class TestManual:

    def test_C(self):
        assert is_prime(10**8 + 7) == True

    def test_D(self):
        assert is_prime(10**10 + 19) == True

    def test_E(self):
        assert is_prime(10**12 + 39) == True

