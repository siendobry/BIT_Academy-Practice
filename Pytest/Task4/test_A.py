import pytest
from function import square


class TestMini:

    def test_1(self):
        assert square(-6) == 36

    def test_2(self):
        assert square(-1) == 1

    def test_3(self):
        assert square(9) == 81


class TestSmall:

    def test_1(self):
        assert square(-961) == 961**2

    def test_2(self):
        assert square(-56) == 56**2

    def test_3(self):
        assert square(225) == 225**2


class TestMed:

    def test_1(self):
        assert square(23454) == 23454**2

    def test_2(self):
        assert square(654333) == 654333**2

    def test_3(self):
        assert square(3456456) == 3456456**2

@pytest.mark.skipif(True, reason="Incorrect results - stopping testing")
class TestMega:

    def test_1(self):
        assert square(10**12) == 10**24

    def test_2(self):
        assert square(10**13) == 10**26

    def test_3(self):
        assert square(10**14) == 10**28

# Napisać 4 klasy funkcji square
# Pierwsza zawiera kilka testów dla losowych liczb z przedziału <-10, 10>
# Druga zawiera kilka testów dla losowych liczb z przedziału <-1000, 1000>
# Trzecia zawiera kilka testów dla losowych liczb z przedziału <10 ** 4, 10 ** 6>
# Czwarta zawiera kilka testów dla losowych liczb z przedziału <10 ** 12, 10 ** 13>
# oraz marker skipif, który po wykonaniu uniemożliwi wykonanie testów z czwartej klasy
# ze względu na niepoprawne działanie funkcji w trzeciej klasie