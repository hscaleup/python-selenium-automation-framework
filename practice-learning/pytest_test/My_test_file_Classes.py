import pytest

class TestClass:

    @classmethod
    def setup_class(cls):
        print("\nSetting up TestClass")

    @classmethod
    def teardown_class(cls):
        print("\nTearing up TestClass")



    def setup_method(self,method):
        if method == self.test1:
            print("\nSetting up Test1!")
        elif method == self.test2:
            print("\nSetting up Test2!")
        else:
            print("\nSetting up Unknown Test!")

    def teardown_method(self,method):
        if method == self.test1:
            print("\nTearing up Test1!")
        elif method == self.test2:
            print("\nTearing up Test2!")
        else:
            print("\nTearing up Unknown Test!")

    def test1(self):
        print("Executing Test1")
        assert True

    def test2(self):
        print("Executing Test2")
        assert True