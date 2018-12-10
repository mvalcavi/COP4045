class Product:
    def __init__(self, name="", price=0.0):
            self.name = name
            self.price = price

class Items:
    def __init__(self, name=None):
        self.title = name


class LineItem:
    def __init__(self, product=None, quantity=1):
            self.product = product
            self.quantity = quantity

    def getTotal(self):
        total = self.price * self.quantity
        return total

class Cart:
    def __init__(self):
        self.__lineitems = []

    def addItem(self, item):
        self.__lineitems.append(item)

    def removeItem(self, index):
        self.__lineitems.pop(index)

    def getTotal(self):
        total = 0.0
        for item in self.__lineitems:
            total += item.getTotal()
        return total

    def getItemCount(self):
        return len(self.__lineitems)

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__lineitems)-1:
            raise StopIteration
        self.__index += 1
        lineitem = self.__lineitems[self.__index]
        return lineitem
