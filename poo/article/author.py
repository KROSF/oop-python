class Author:
    def __init__(self, name, lastname, address):
        self.__name = name
        self.__lastname = lastname
        self.__address = address

    @property
    def name(self) -> str:
        return self.__name

    @property
    def lastname(self) -> str:
        return self.__lastname

    @property
    def address(self) -> str:
        return self.__address

    def __str__(self):
        return self.__lastname
