from func import func1, func2

def test_func1(func1):
    assert func1(2, 4) == 6


def test_func2(func2):
    assert func2(2, 4) == 8