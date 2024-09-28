class Checkout:
    class Discount:
        def __init__(self, noOfItems, price):
            self.noOfItems = noOfItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}
        self.total = 0
    
    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item in self.items:
            self.items[item] +=1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total =0
        for item, cnt in self.items.items():
            total += self.prices[item]* cnt
        return total
    
    def addDiscount(self, item, noOfItems, price):
        discount = self.Discount(noOfItems, price)
        self.discounts[item] = discount