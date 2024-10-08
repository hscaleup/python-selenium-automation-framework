import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a",1)
    checkout.addItemPrice("b",2)
    return checkout

def test_calculateTotal(checkout):
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1

def test_getCorrectTotalFromMultipleItemsAdded(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3

def test_canAddDiscountRule(checkout):
    checkout.addDiscount("a",3,2)

@pytest.mark.skip
def test_canApplyDiscountRule(checkout):
    checkout.addDiscount("a",3,2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1


