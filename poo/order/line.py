class Line:
    def __init__(self, price: float, amount: int = 1):
        self.__price = price
        self.__amount = amount

    @property
    def price(self):
        return self.__price

    @property
    def amount(self):
        return self.__amount

    def __str__(self):
        return "{:.2f} €\t\t{}".format(self.price, self.amount)
