import string
from poo.luhn import luhn


class Number:
    def __init__(self, number):
        if not len(number):
            raise NumberException("Invalid lenght")
        number = number.translate({ord(c): None for c in string.whitespace})
        if not number.isdigit():
            raise NumberException("Number should only contain digits")
        if len(number) < 13 or len(number) > 19:
            raise NumberException("Invalid lenght")
        if not luhn(number):
            raise NumberException("Inavalid number for a card")
        self.__number = number

    def __str__(self):
        return self.__number

    def __lt__(self, other):
        return self.__str__() < other.__str__()


class NumberException(Exception):
    """
    Raised on invalid card number, invalid lenght number
    """

    pass
