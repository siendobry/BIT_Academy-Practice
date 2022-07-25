from cmplex import C

def test_1():
    img_num = C(0, 0).__mul__(C(0, 0))
    assert img_num.x == 0 and img_num.y == 0

def test_2():
    img_num = C(5, 10).__mul__(C(1, 2))
    assert img_num.x == -15 and img_num.y == 20

def test_3():
    img_num = C(100, 0).__mul__(C(0, 20))
    assert img_num.x == 0 and img_num.y == 2000

def test_4():
    img_num = C(15, 20).__mul__(C(15, 20))
    assert img_num.x == -175 and img_num.y == 600

# Napisać testy sprawdzające mnożenie liczb zespolonych
# w załączonym pliku