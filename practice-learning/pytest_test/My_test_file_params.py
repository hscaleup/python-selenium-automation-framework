import pytest


@pytest.fixture(params=[1,2,3])
def setUp(request):
    retVal = request.param
    print("\nSetUp! retval = {}".format(retVal))
    return retVal

def test2(setUp):
    print("\nSetUp = {}".format(setUp))
    assert True