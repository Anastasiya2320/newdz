import pytest
from dz13.hw13 import Time

@pytest.mark.parametrize("time1, time2, expected_sum", [
    (Time(1, 30, 45), Time(2, 15, 20), Time(3, 46, 5)),
    (Time(22, 58, 58), Time(4, 4, 4), Time(3, 3, 2)),
])
def test_addition(time1, time2, expected_sum):
    result = time1 + time2
    assert result == expected_sum

@pytest.mark.parametrize("time1, time2, expected_sup", [
    (Time(5, 30, 45), Time(2, 15, 20), Time(3, 15, 25)),
    (Time(0, 0, 0), Time(0, 2, 0), Time(23, 58, 00)),
])

def test_sub(time1, time2, expected_sup):
    result = time1 - time2
    assert result == expected_sup

@pytest.mark.parametrize("time1, time2", [
    (Time(3, 20, 10), Time(3, 20, 10)),
    (Time(4, 10, 15), Time(4, 10, 15)),
])
def test_equality(time1, time2):
    assert time1 == time2

@pytest.mark.parametrize("time1, time2", [
    (Time(4, 10, 15), Time(4, 10, 20)),
    (Time(1, 30, 45), Time(2, 15, 20)),
])
def test_inequality(time1, time2):
    assert time1 != time2
