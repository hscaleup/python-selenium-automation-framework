import pytest
from pytest import approx
from pytest import raises

def test_IntAssert():
    assert 1 ==1;

def test_floatAssert():
    value= 0.2 + 0.3
    assert value == 0.5

def test_strAssert():
    assert 'str' == "str"

def test_ArrayAsset():
    arr = [1,2,3]
    assert arr ==[1,2,3]

def test_dicAssert():
    dic = {"1":1}
    assert dic =={"1":1}

def test_float():
    assert (0.1 + 0.3)== approx(0.4)

def raiseValueException():
    raise ValueError

def test_exception():
        with raises(ValueError):
             raiseValueException()