import pytest

@pytest.fixture(scope="session", autouse=True)
def setUpSession():
    print("\nSetUp Session")

@pytest.fixture(scope="module", autouse=True)
def setUpModule():
    print("\nSetUp Module")

@pytest.fixture(scope="function", autouse=True)
def setUpFunction():
    print("\nSetUp function")


def test1():
    print("Executing Test1")
    assert True

def test2():
    print("Executing Test2")
    assert True