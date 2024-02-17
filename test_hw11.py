from dz11.hw11 import Time

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
























