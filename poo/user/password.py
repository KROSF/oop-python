from passlib.context import CryptContext


class Password:
    __ctx = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000,
    )

    def __init__(self, password):
        if len(password) < 8:
            raise PasswordException("Password is too short. (min: 8).")
        self.__password = self.__ctx.encrypt(password)

    def __str__(self):
        return self.__password

    def verify(self, password):
        return self.__ctx.verify(password, self.__password)


class PasswordException(Exception):
    """
    Raised when password is to short or error on encrypt
    """

    pass
