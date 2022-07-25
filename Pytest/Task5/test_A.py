import pytest
from function import count_chars


@pytest.mark.parametrize("word, output", [("aaabc", [3, 1, 1]), ("acbabcabcbcb", [3, 5, 4]),
                                          ("akisrvbasdrukvbabhdr", [3, 3, 0]), ("piespiespiespiespies", [0, 0, 0])])
def tests(word, output):
    assert count_chars(word) == output

# Napisać testy dla funkcji count_chars za pomocą
# markera "parametrize"

# Funkcja count_chars zwraca trzyelementową tablicę
# która zawiera odpowiednio liczbę wystąpień znaku 'a', 'b' i 'c'
