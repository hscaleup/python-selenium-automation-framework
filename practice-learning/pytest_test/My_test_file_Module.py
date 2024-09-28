import pytest

def setup_class(module):
    print("\nSetting up Module")

def teardown_module(module):
    print("\nTearing up Module \n")

def setup_function(function):
    if function == test1:
        print("\nSetting up Test1!")
    elif function == test2:
        print("\nSetting up Test2!")
    else:
        print("\nSetting up Unknown Test!")

def teardown_function(function):
    if function == test1:
        print("\nTearing up Test1!")
    elif function == test2:
        print("\nTearing up Test2!")
    else:
        print("\nTearing up Unknown Test!")

def test1():
    print("Executing Test1")
    assert True

def test2():
    print("Executing Test2")
    assert True