class User:
    users = set()

    def __init__(self, id, name, lastname, address, password):
        self.__id = id
        self.__name = name
        self.__lastname = lastname
        self.__address = address
        self.__password = password
        self.__cards = {}
        self.__articles = {}
        self.users.add(id)

    def __copy__(self):
        raise Exception("User cannot be copied")

    def __deepcopy__(self, memo):
        raise Exception("User cannot be copied")

    def __del__(self):
        for card in self.__cards.values():
            card.remove_holder()
        self.users.remove(self.__id)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def lastname(self):
        return self.__lastname

    @property
    def address(self):
        return self.__lastname

    @property
    def articles(self):
        return self.__articles

    @property
    def articles_amount(self):
        return len(self.__articles)

    def buy(self, article, amount=1):
        if not amount:
            self.__articles.pop(article, None)
        else:
            self.__articles[article] = amount

    def has(self, card):
        if self is card.user:
            self.__cards[card.number] = card

    def remove(self, card):
        if card.number in self.__cards:
            card.remove_holder()
            self.__cards.pop(card)

    def show_cart(self):
        pattern = " shopping cart of {} [Articles: {}]\n Amount.  Article\n {}\n"
        result = pattern.format(self.id, self.articles_amount, "=" * 95)
        pattern = ' {a:04d}     [{r}] "{t}", {y}. {p:.2f} €\n'
        for article, amount in self.articles.items():
            result += pattern.format(
                a=amount,
                r=article.ref,
                t=article.title,
                y=article.pub_date.year,
                p=article.price,
            )
        return result
