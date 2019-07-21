from parse import search
from datetime import datetime, timedelta
from copy import deepcopy


class Date:
    def __init__(self, day=0, month=0, year=0):
        if isinstance(day, Date):
            self.__dict__ = deepcopy(day).__dict__
        elif isinstance(day, str):
            self.__from_str(day)
        else:
            self.__day = day
            self.__month = month
            self.__year = year
        self.__from_system()
        self.__is_valid()

    def __from_str(self, string):
        parsed = search("{day:2d}/{month:2d}/{year:4d}", string)
        if parsed is None:
            raise DateException("format of string invalid")
        self.__day = parsed["day"]
        self.__month = parsed["month"]
        self.__year = parsed["year"]

    def __is_valid(self):
        try:
            datetime(self.year, self.month, self.day)
        except ValueError as e:
            raise DateException(str(e))

    def __from_system(self):
        now = datetime.now()
        if self.__day == 0:
            self.__day = now.day
        if self.__month == 0:
            self.__month = now.month
        if self.__year == 0:
            self.__year = now.year

    @property
    def day(self) -> int:
        return self.__day

    @property
    def month(self) -> int:
        return self.__month

    @property
    def year(self) -> int:
        return self.__year

    def __iadd__(self, days):
        if not isinstance(days, int):
            raise DateException("int value is required")
        try:
            date = datetime(self.year, self.month, self.day) + timedelta(days=days)
        except OverflowError as e:
            raise DateException(str(e))
        self.__day = date.day
        self.__month = date.month
        self.__year = date.year
        return self

    def __isub__(self, days):
        self.__iadd__(-days)
        return self

    def __add__(self, days):
        date = Date(self)
        return date.__iadd__(days)

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        elif self.month < other.month:
            return True
        elif self.month > other.month:
            return False
        else:
            return self.day < other.day

    def __gt__(self, other):
        return other.__lt__(self)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __eq__(self, other):
        return (
            self.day == other.day
            and self.month == other.month
            and self.year == other.year
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        date = datetime(self.year, self.month, self.day)
        return date.strftime("%A %d %B %Y")


class DateException(Exception):
    """
    Raised when Date format is not valid.
    """

    pass
