from abc import abstractmethod


class ArticleException(Exception):
    pass


class Article:
    def __init__(self, authors, ref, title, pub_date, price):
        if len(authors) == 0:
            raise ArticleException("At least one author must be provided")
        self.__authors = authors
        self.__ref = ref
        self.__title = title
        self.__pub_date = pub_date
        self.__price = price

    @property
    def authors(self):
        return self.__authors

    @property
    def ref(self):
        return self.__ref

    @property
    def title(self):
        return self.__title

    @property
    def pub_date(self):
        return self.__pub_date

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):  # noqa
        self.__price = price

    @abstractmethod
    def specific_print(self) -> str:
        pass

    def __str__(self):
        pattern = (
            '[{ref}] "{title}", from {authors}. {year}. {price:.2f} €\n{sp} {specific}.'
        )
        return pattern.format(
            ref=self.ref,
            title=self.title,
            authors=", ".join(map(str, self.authors)),
            year=self.pub_date.year,
            price=self.price,
            sp=" " * 5,
            specific=self.specific_print(),
        )


class PsycalArticle(Article):
    def __init__(self, authors, ref, title, pub_date, price, stock=0):
        self.__stock = stock
        Article.__init__(self, authors, ref, title, pub_date, price)

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):  # noqa
        self.__stock = stock


class Book(PsycalArticle):
    def __init__(self, authors, ref, title, pub_date, price, pages, stock=0):
        self.__pages = pages
        PsycalArticle.__init__(self, authors, ref, title, pub_date, price, stock)

    @property
    def pages(self):
        return self.__pages

    def specific_print(self) -> str:
        return "This book has {} pages and there are {} units in stock".format(
            self.pages, self.stock
        )


class USB(PsycalArticle):
    def __init__(self, authors, ref, title, pub_date, price, size, stock=0):
        self.__size = size
        PsycalArticle.__init__(self, authors, ref, title, pub_date, price, stock)

    @property
    def size(self):
        return self.__size

    def specific_print(self) -> str:
        return "This usb has {} MB and there are {} units in stock".format(
            self.size, self.stock
        )


class DigitalArticle(Article):
    def __init__(self, authors, ref, title, pub_date, price, expire_date):
        self.__expire_date = expire_date
        Article.__init__(self, authors, ref, title, pub_date, price)

    @property
    def expire_date(self):
        return self.__expire_date

    @expire_date.setter
    def expire_date(self, expire_date):  # noqa
        self.__expire_date = expire_date


class EBook(DigitalArticle):
    def __init__(self, authors, ref, title, pub_date, price, expire_date):
        DigitalArticle.__init__(self, authors, ref, title, pub_date, price, expire_date)

    def specific_print(self) -> str:
        return "this ebook will be on sale until {}".format(self.expire_date)
