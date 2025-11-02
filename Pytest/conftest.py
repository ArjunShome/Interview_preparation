import pytest

@pytest.fixture()
def return_int_val():
    return 1, 3

@pytest.fixture()
def return_str_val():
    return "My Name is", " Arjun Shome"