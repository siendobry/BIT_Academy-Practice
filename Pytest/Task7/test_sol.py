from solution import selsort
from random import randint
import pytest


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def get_res(p):
    output = []
    while p is not None:
        output.append(p.val)
        p = p.next
    output.sort()
    return output


def gen_list(b):
    if not b:
        size = randint(10**2, 10**3)
        nums = (-(10**4), 10**4)
    else:
        size = randint(10**3, 10**4)
        nums = (-(10**6), 10**6)
    p = Node(randint(nums[0], nums[1]))
    for i in range(size):
        x = Node(randint(nums[0], nums[1]))
        x.next = p.next
        p.next = x
    return p

class TestBasic:

    def test_A(self):
        assert selsort(None) is None

    def test_B(self):
        l = Node(5)
        assert selsort(l).val == 5

    def test_C(self):
        l = Node(5)
        l.next = Node(2)
        l = selsort(l)
        output = []
        while l is not None:
            output.append(l.val)
            l = l.next
        assert output == [2, 5]


class TestAuto:

    @pytest.mark.parametrize("llist", [gen_list(False) for _ in range(4)])
    def test_D(self, llist):
        res = get_res(llist)
        p = selsort(llist)
        r = p.next
        output = [p.val]
        while r is not None:
            output.append(r.val)
            r = r.next
        assert output == res

    @pytest.mark.parametrize("llist", [gen_list(True) for _ in range(3)])
    def test_E(self, llist):
        res = get_res(llist)
        p = selsort(llist)
        r = p.next
        output = [p.val]
        while r is not None:
            output.append(r.val)
            r = r.next
        assert output == res
