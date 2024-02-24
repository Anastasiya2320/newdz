import pytest
from dz11.hw11 import Time

@pytest.mark.parametrize("hours, minutes, seconds, expected_hours, expected_minutes, expected_seconds", [
    (10, 30, 45, 10, 30, 45),  # Valid input values
    (25, 70, -5, 0, 0, 0),      # Invalid input values
])
def test_input_time(hours, minutes, seconds, expected_hours, expected_minutes, expected_seconds):
    t = Time()
    t.h = hours
    t.m = minutes
    t.s = seconds
    assert t.h == expected_hours
    assert t.m == expected_minutes
    assert t.s == expected_seconds

def test_input_time(mocker):
    mocker.patch("builtins.input", return_value = 1)
    t = Time()
    t.input_time()
    assert t.h == 1
    assert t.m == 1
    assert t.s == 1


def test_str_(mocker):
    t = Time(13, 5, 34)
    assert str(t) == 'время: 13:05:34'
   
   
      























