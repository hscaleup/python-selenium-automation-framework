import pytest


def fizzBuzz(value):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    elif isMultiple(value, 5):
        return "Buzz"
    else:
        return str(value)
    
def isMultiple(value, mod):
    return(value % mod) == 0



def checkFizzBuzz(value, expectedValue):
    returnValue = fizzBuzz(value)
    assert returnValue == expectedValue



def test_return1whenpass1():
    checkFizzBuzz(1,"1")
   

def test_return2whenpass2():
    checkFizzBuzz(2, "2")

def test_returnFizzwhenpass3():
    checkFizzBuzz(3, "Fizz")

def test_returnBuzzwhenpass5():
    checkFizzBuzz(5, "Buzz")

def test_returnFizzwhenpass6():
    checkFizzBuzz(6, "Fizz")

def test_returnBuzzwhenpass10():
    checkFizzBuzz(10, "Buzz")

def test_returnFizzBuzzwhenpass15():
    checkFizzBuzz(15, "FizzBuzz")