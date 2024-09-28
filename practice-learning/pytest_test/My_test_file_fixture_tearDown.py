import pytest

@pytest.fixture
def setUp1():
     print("\nsetup 1")
     yield
     print("\nTeardown 1")

@pytest.fixture
def setUp2(request):
    print("\nsetup 2")

    def teardown_a():
        print("\nTearDown A")

    def teardown_b():
        print("\nTearDown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test1(setUp1):
    print("Executing Test1")
    assert True

def test2(setUp2):
    print("Executing Test2")
    assert True