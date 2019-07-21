class UserOrder:
    def __init__(self):
        self.__order_user = {}
        self.__user_orders = {}

    def associate(self, user, order):
        if user in self.__user_orders:
            self.__user_orders[user].add(order)
        else:
            self.__user_orders[user] = set([order])
        self.__order_user[order] = user

    def orders(self, user):
        return self.__user_orders[user]

    def client(self, order):
        return self.__order_user[order]
