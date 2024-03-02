import pytest
from dz11.hw11 import Time


def test_input_time(mocker):
    mocker.patch("builtins.input", return_value = 1)
    t = Time()
    t.input_time()
    assert t.h == 1
    assert t.m == 1
    assert t.s == 1


def test_init_(mocker):
    t = Time(13, 5, 34)
    assert t.h == 13
    assert t.m == 5
    assert t.s == 34


@pytest.mark.parametrize("hours, minutes, seconds, expected_str",
                         [(13, 5, 34, 'время: 13:05:34'),
                          (8, 15, 0, 'время: 08:15:00'),
                          (1, 1, 1, 'время: 01:01:01')
                          (23, 59, 59, 'время: 23:59:59')])
def test_str_(hours, minutes, seconds, expected_str):
    t = Time(hours, minutes, seconds)
    assert str(t) == expected_str


def test_input_time_with_invalid_values(mocker):
    mocker.patch("builtins.input", return_value = 24)
    t = Time()
    with pytest.raises(ValueError):
        t.input_time()






















