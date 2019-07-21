from .line import Line


class ArticleOrder:
    def __init__(self):
        self.__order_items = {}
        self.__article_orders = {}

    def order(self, order, article, price, amount=1):
        order_line = Line(price, amount)
        if order in self.__order_items:
            self.__order_items[order][article] = order_line
        else:
            self.__order_items[order] = {article: order_line}
        if article in self.__article_orders:
            self.__article_orders[article][order] = order_line
        else:
            self.__article_orders[article] = {order: order_line}

    def details(self, order):
        return self.__order_items[order]

    def sales(self, article):
        return self.__article_orders[article]

    def details_str(self) -> str:
        total = 0.0
        pattern = "Order #: {}\nClient: {}\tDate: {}\n{}"
        result = ""
        for order, items in self.__order_items.items():
            result += pattern.format(
                order.number, order.card.holder, order.date, self.__items(items)
            )
            total += order.total
        result += "\nTOTAL SALES:\t {:.2f} €\n".format(total)
        return result

    def sales_str(self) -> str:
        pattern = 'Sales of [{}] "{}"\n{}\n'
        result = ""
        for article, orders in self.__article_orders.items():
            result += pattern.format(article.ref, article.title, self.__orders(orders))
        return result

    def __items(self, items) -> str:
        total = 0.0
        result = "\n{line}\n  PVP\t\tAmount\tArticle\n{line}\n".format(line="=" * 66)
        pattern = '{}\t[{}] "{}"\n'
        for article, line in items.items():
            result += pattern.format(str(line), article.ref, article.title)
            total += line.price * line.amount
        result += "{}\nTotal\t{:.2f} €\n\n".format("=" * 66, total)
        return result

    def __orders(self, orders) -> str:
        amount = 0
        total = 0.0
        result = "[Orders: {len}]\n{line}\n  PVP\t\tAmount\t\tDate\n{line}\n".format(
            line="=" * 66, len=len(orders)
        )
        pattern = "{}\t\t{}\n"
        for order, line in orders.items():
            result += pattern.format(line, str(order.date))
            total += line.price * line.amount
            amount += line.amount
        result += "{}\n{:.2f} €\t{}\n".format("=" * 66, total, amount)
        return result
