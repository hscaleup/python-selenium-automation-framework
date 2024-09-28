import pytest


@pytest.fixture(autouse=True)
def setupAuto():
    print("\nSetupAuto")

@pytest.fixture
def setup():
    print("\nSetup")

@pytest.fixture
def setUpOther():
    print("\nSetUpOther")

def test1(setUpOther,setup):
    print("Executing Test1")
    assert True

@pytest.mark.usefixtures("setup","setUpOther")
def test2():
    print("Executing Test2")
    assert True