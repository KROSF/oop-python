import re
from enum import Enum
from poo.date import Date


class Brand(Enum):
    UNKNOWN = 0
    VISA = 1
    MASTERCARD = 2
    MAESTRO = 3
    JCB = 4
    AMEX = 5

    def __str__(self):
        if self.value == 5:
            return "AMERICAN EXPRESS"
        return self.name


class Card:
    __BRANDS = {
        Brand.VISA: re.compile(r"^4"),
        Brand.MASTERCARD: re.compile(r"^5"),
        Brand.MAESTRO: re.compile(r"^6"),
        Brand.JCB: re.compile(r"^3[47]"),
        Brand.AMEX: re.compile(r"^3[1235689]"),
    }

    def __init__(self, number, user, date):
        if Date() > date:
            raise CardException("Card has expired")
        self.__number = number
        self.__user = user
        self.__expire = date
        self.__state = True
        self.__brand = self.__get_brand(number)

    def __lt__(self, other):
        return self.number < other.number

    def __get_brand(self, number):
        for brand, regexp in self.__BRANDS.items():
            if regexp.match(str(number)):
                return brand
        return Brand.UNKNOWN

    def __del__(self):
        if hasattr(self, "__user"):
            self.user.remove(self)

    @property
    def brand(self):
        return self.__brand

    @property
    def number(self):
        return self.__number

    @property
    def user(self):
        return self.__user

    @property
    def expire(self):
        return self.__expire

    @property
    def holder(self):
        return "{} {}".format(self.__user.name, self.__user.lastname).upper()

    @property
    def is_active(self):
        return self.__state

    def active(self, state=True):
        self.__state = state

    def remove_holder(self):
        self.__user = None
        self.__state = False


class CardException(Exception):
    """
    Raised when card is expired
    """

    pass
