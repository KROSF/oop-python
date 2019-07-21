from poo.date import Date
from poo.article import EBook, PsycalArticle
from copy import copy


class OrderException(Exception):
    pass


class Order:
    number_of_orders = 0

    def __init__(self, user_order, article_order, user, card, date=Date()):
        self.__total = 0.0
        if user.articles_amount == 0:
            raise OrderException("Amount of article cannot be 0")
        if card.user != user:
            raise OrderException("Card holder is not correct")
        if not card.is_active:
            raise OrderException("Card is not active")
        if date > card.expire:
            raise OrderException("Card is expire")
        is_empty = True
        cart = copy(user.articles)
        for article, amount in cart.items():
            if isinstance(article, EBook):
                if article.expire_date < Date():
                    user.buy(article, 0)
                else:
                    article_order.order(self, article, article.price, amount)
                    self.__total += article.price * amount
                    user.buy(article, 0)
                    is_empty = False
            elif isinstance(article, PsycalArticle):
                if article.stock < amount:
                    user.articles.clear()
                    raise OrderException("Article currently has not stock")
                article.stock -= amount
                article_order.order(self, article, article.price, amount)
                self.__total += article.price * amount
                user.buy(article, 0)
                is_empty = False
            else:
                raise OrderException("Unknown article")
        if is_empty:
            raise OrderException("Order is empty")
        user_order.associate(user, self)
        self.__number = self.number_of_orders
        self.__card = card
        self.__date = date
        Order.number_of_orders = Order.number_of_orders + 1

    @property
    def number(self):
        return self.__number

    @property
    def card(self):
        return self.__card

    @property
    def date(self):
        return self.__date

    @property
    def total(self):
        return self.__total

    def __str__(self):
        return (
            "Order #: {:<13}\nDate: {:<13}\nPaid with: {} {}\nAmount: {:.2f} €\n"
        ).format(
            self.number,
            str(self.date),
            str(self.card.brand),
            str(self.card.number),
            self.total,
        )
