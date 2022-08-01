from cmplex import C

def test_1():
    img_num = C(0, 0).__add__(C(1, 2))
    assert img_num.x == 1 and img_num.y == 2

def test_2():
    img_num = C(5, 10).__add__(C(20, 54))
    assert img_num.x == 25 and img_num.y == 64

def test_3():
    img_num = C(-58, 3).__add__(C(6, -20))
    assert img_num.x == -52 and img_num.y == -17

def test_4():
    img_num = C(-7, -67).__add__(C(100, 50))
    assert img_num.x == 93 and img_num.y == -17

# Napisać testy sprawdzające dodawanie liczb zespolonych
# w załączonym pliku