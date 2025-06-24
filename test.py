# test_math_operations.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def test_addition():
    assert add(1, 1) == 3 # Intentionally wrong assertion
    assert add(0, 5) == 5
    assert add(-1, 1) == 0

def test_subtraction():
    assert subtract(3, 1) == 2
    assert subtract(5, 3) == 2
    assert subtract(1, 5) == -4

def test_addition_and_subtraction():
    assert add(3, 4) - subtract(2, 1) == 6