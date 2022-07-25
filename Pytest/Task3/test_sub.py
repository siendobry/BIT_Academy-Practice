from cmplex import C

def test_1():
    img_num = C(0, 0).__sub__(C(1, 2))
    assert img_num.x == -1 and img_num.y == -2

def test_2():
    img_num = C(5, 10).__sub__(C(20, 54))
    assert img_num.x == -15 and img_num.y == -44

def test_3():
    img_num = C(-58, 3).__sub__(C(6, -20))
    assert img_num.x == -64 and img_num.y == 23

def test_4():
    img_num = C(-7, -67).__sub__(C(100, 50))
    assert img_num.x == -107 and img_num.y == -117

# Napisać testy sprawdzające odejmowanie liczb zespolonych
# w załączonym pliku