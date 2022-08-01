from solution import next_prime
from random import randint
import pytest


def check_prime(y):
    y += 1

    def is_prime(x):
        if x < 2:
            return False
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True

    while not is_prime(y):
        y += 1
    return y


def pair_gen():
    val = randint(10**9, 10**12)
    return val, next_prime(val)


class TestManual:

    @pytest.mark.parametrize("value, output", [(0, 2), (5, 7), (10, 11)])
    def test_A(self, value, output):
        assert next_prime(value) == output

    @pytest.mark.parametrize("value, output", [(10**6, 10**6 + 3), (10**9, 10**9 + 7), (10**12, 10**12 + 39)])
    def test_B(self, value, output):
        assert next_prime(value) == output


class TestAutomatic:

    @pytest.mark.parametrize("value, output", [pair_gen() for _ in range(4)])
    def test_C(self, value, output):
        assert next_prime(value) == output
