import pytest

# documentation of command line argumements
# -v : verbose
# -s : Dont show console output, it only shows print statement
# -q: run in quiet mode 100 of tests in one go
# --ignore : to ignore specified paths
# --maxfail : stop after specified no of failures
# pytest -v -s  test_file2.py to test all test in single module
# pytest -v -s -k "test1 or test3" to run particular or combination of test from diffetent modules
# pytest -v -s -m "reg or reg2" run single or combination of test using marker  @pytest.mark.reg/@pytest.mark.reg2 

@pytest.mark.reg
def test1():
    print("Executing Test1")
    assert True
