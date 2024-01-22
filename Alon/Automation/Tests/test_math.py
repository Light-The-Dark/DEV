import pytest


# def test_sum():
#     assert 1 + 1 == 2


# def test_2():
#     a = 1
#     b = 2
#     c = 3
#     assert a + b == c


def divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
        print(num)
    assert 'division by zero' in str(e.value)
