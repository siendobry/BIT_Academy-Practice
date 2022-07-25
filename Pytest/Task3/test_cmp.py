from cmplex import C

def test_1():
    assert C(0, 0).__eq__(C(0, 0)) == True

def test_2():
    assert C(2, 30).__eq__((C(3, 20))) == False

def test_3():
    assert C(58, 26).__eq__(C(58, 25)) == False

def test_4():
    assert C(-12, 5).__eq__(C(12, -5)) == False

# Napisać testy sprawdzające porównywanie liczb zespolonych
# w załączonym pliku