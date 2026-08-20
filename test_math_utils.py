from math_utils import add, check_status, divide, multiply, subtract


def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(5,3) == 2

def test_multiply():
    assert multiply(3,4) == 12

def test_devide():
    assert divide(4,2) == 2

def test_check_status():
    assert check_status(200) == "OK"
