import pytest

@pytest.fixture(scope="class", autouse=True)
def setUpClass2():
    print("\nSetUp class2")

@pytest.fixture(scope="module", autouse=True)
def setUpModule2():
    print("\nSetUp Module2")

@pytest.fixture(scope="function", autouse=True)
def setUpFunction2():
    print("\nSetUp function2")



class TestClass:

    
    def test1(self):
        print("Executing Test1")
        assert True

    def test2(self):
        print("Executing Test2")
        assert True