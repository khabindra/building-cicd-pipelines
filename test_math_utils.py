from math_utils import add, divide, multiply, subtract

url = "https://github.com"  # Dummy line, can stay or be removed

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(4, 2) == 2
