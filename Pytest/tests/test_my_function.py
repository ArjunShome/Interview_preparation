import pytest
import Pytest.app.my_functions as my_func


def test_add(return_int_val):
    assert my_func.add(return_int_val[0], return_int_val[1]) == 4

def test_add_negative(return_int_val):
    assert my_func.add(return_int_val[0], return_int_val[1]) != 6

def test_sum_str(return_str_val):
    assert my_func.sum(return_str_val[0], return_str_val[1]) == "My Name is Arjun Shome"

@pytest.mark.skip(reason="Skipping this test for now")
def test_sum_skipped(return_int_val):
    assert my_func.sum(return_int_val[0], return_int_val[1]) == 4

@pytest.mark.parametrize("num1, num2, expected", [(1, 3, 4), (2, 4, 6), (5, 5, 10)])
def test_sum_parameterized(num1, num2, expected):
    assert my_func.add(num1, num2) == expected

def test_add_exception():
    with pytest.raises(ValueError):
        my_func.add('qwerty', 1)