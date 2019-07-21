from poo.date import Date
from poo.card import Card, Number, CardException
from poo.user import User, Password
from poo.order import UserOrder, ArticleOrder, Order, OrderException
from poo.article import Author, Book, EBook, USB, ArticleException

lucas = User(
    "lucas",
    "Lucas",
    "Grijánder",
    "Avda. Generalísimo, 654 (Barbate)",
    Password("vaeg0Quo"),
)

krispin = User(
    "krispin", "Crispín", "Klánder", "C/ del Jurel, 876 (Barbate)", Password("Pheaj9li")
)

yoshua = User(
    "yoshua",
    "Yoshua",
    "Tri Padváisor",
    "Callejón de los negros, s/n (Cádiz)",
    Password("ahxo2Aht"),
)

yessi = User(
    "yessi",
    "Yésica",
    "Brona Gomes",
    "C/ de Sor Sofía, 345 (2 Hermanas)",
    Password("Roh9aa5v"),
)

dinners = Card(Number("30569309025904"), yessi, Date(31, 7) + 5 * 365)
visa = Card(Number("4539 4512 0398 7356"), lucas, Date(31, 12, 0) + 3 * 365)
amex = Card(Number("378282246310005"), yoshua, Date(30, 11, 0) + 4 * 365)
mastercard = Card(Number("555555555555 4444  "), krispin, Date(31, 1) + 3 * 365)
aus_bank = Card(Number("5610591081018250"), krispin, Date(28, 2) + 365)
jcb = Card(Number("3530111333300000"), yessi, Date("31/7/0") + 2 * 365)
visa_2 = Card(Number(" 4222222222222"), lucas, Date("28/2/0") + 365)

Pepe = Author("Pepe", "Leches", "Avda. del Pollo, 55 (Barbate)")
Marchena = Author("Marchena", "Picuito", "Callejón de los Negros, 5 (Ubrique)")
Carlos = Author("Carlos", "El Legionario", "C/M.ª Arteaga, 155 (Bornos)")
Carmela = Author("La Uchi", "Poyáquez", "Callejón Circo, 45 (Cádiz)")

arte_insulto = Book(
    set([Marchena]), "100", "El arte del insulto", Date("1/8/2000"), 32.50, 245, 5
)

montar_bici = Book(
    set([Carmela]),
    "110",
    "Cómo montar en bici sin sillín",
    Date("20/6/1998)"),
    35.95,
    650,
    100,
)

braille = Book(
    set([Pepe]),
    "111",
    "Aprenda Braille en 5 minutos",
    Date("5/10/2002"),
    42.10,
    150,
    300,
)

baston = Book(
    set([Pepe, Carlos]), "103", "Historia del bastón", Date("1/2/2001"), 39.95, 455, 4
)

ebook = EBook(
    set([Pepe, Carlos]), "034", "Revisiones", Date("15/1/2009"), 6.0, Date("1/7/2009")
)

ebook_2 = EBook(
    set([Carmela]),
    "035",
    "Horarios",
    Date("20/3/2009)"),
    9.0,
    Date("20/6/00") + 365 * 4,
)

ebook_3 = EBook(
    set([Carmela]), "036", "Exámenes", Date("1/10/2007"), 12.0, Date("30/9/2008")
)

usb = USB(set([Carmela]), "210", "Camela", Date("1/8/2000"), 32.50, 245, 40)

usb_2 = USB(
    set([Carmela, Marchena]),
    "211",
    "Mecano nlaleche",
    Date("20/6/1998"),
    35.95,
    650,
    50,
)

usb_3 = USB(
    set([Carmela, Marchena, Pepe]),
    "220",
    "Jarabe de Falo",
    Date("7/7/2007"),
    12.90,
    547,
    30,
)

print("\n---------------INVENTARIO DE EXISTENCIAS-----------\nLIBROS:\n")
print(arte_insulto, montar_bici, braille, baston, sep="\n\n")

user_order = UserOrder()
article_order = ArticleOrder()

print("\n\nCARRITOS VACÍOS\n")
print(lucas.show_cart())
print(krispin.show_cart())
print(yoshua.show_cart())
print(yessi.show_cart())

lucas.buy(montar_bici, 3)
lucas.buy(braille, 1)
lucas.buy(ebook, 2)
lucas.buy(usb_2, 1)

print(lucas.show_cart())

order = Order(user_order, article_order, lucas, visa, Date(10, 3))

print("*** Cambio de precio de MONTAR_BICI, BRAILLE, EBOOK y USB\n")
montar_bici.price = 29.95
braille.price = 44.50
ebook.price = 5.50
usb.price = 24.05

krispin.buy(montar_bici, 2)
krispin.buy(braille, 2)
print(krispin.show_cart())

print("\n*** krispin devuelve BRAILLE y compra ARTE_INSULTO y USB_3")
krispin.buy(braille, 0)
krispin.buy(arte_insulto)
krispin.buy(usb_3)
print(krispin.show_cart())

print(
    "\n*** No se comprueban existencias\n*** existencias de BASTON = {}".format(
        baston.stock
    )
)

yoshua.buy(baston, 6)

print("\n*** No se comprueba la fecha de expiración")
print("*** fecha expir. ebook_3 = {}".format(ebook_3.expire_date))

yoshua.buy(ebook_3, 2)
print(yoshua.show_cart())

print("\n*** Yoshua devuelve 4 BASTON")
yoshua.buy(baston, 2)
print(yoshua.show_cart())
yesterday = Date()
yesterday -= 1
order_2 = Order(user_order, article_order, yoshua, amex, yesterday)
order_3 = Order(user_order, article_order, krispin, mastercard, Date("5/4/2010"))

print("*** Cambio de precio de ARTE_INSULTO, BASTON y ebook_2\n")
arte_insulto.price = 35.20
baston.price = 34.9
ebook_2.price = 3.0

yessi.buy(usb_3, 2)
yessi.buy(ebook_2, 3)
yessi.buy(braille)
yessi.buy(usb_2, 0)
print(yessi.show_cart())

order_4 = Order(user_order, article_order, yessi, jcb, Date("5/4/2010"))

print("\n---------------------PEDIDOS-----------------------")

print(order, order_2, order_3, order_4, sep="\n")

arte_insulto.stock += 5
montar_bici.stock *= 4
braille.stock += 2
baston.stock += 2


yessi.buy(braille)
yessi.buy(baston)
order_5 = Order(user_order, article_order, yessi, jcb)
yessi.buy(montar_bici, 3)
order_6 = Order(user_order, article_order, yessi, dinners)
krispin.buy(baston)
krispin.buy(braille)
krispin.buy(arte_insulto, 3)
order_7 = Order(user_order, article_order, krispin, aus_bank, Date("5/4/2010"))
yoshua.buy(arte_insulto, 2)
yoshua.buy(montar_bici)
order_8 = Order(user_order, article_order, yoshua, amex, Date("5/4/2010"))

print(order_5, order_6, order_7, order_8, sep="\n")
print("\n-------------------DETALLE DE PEDIDOS--------------")
print(article_order.details_str())
print("\n------------------VENTAS DE ARTÍCULOS--------------")
print(article_order.sales_str())
print("\n-----------------PRUEBAS DE EXCEPCIONES------------")

try:
    null = Order(user_order, article_order, lucas, visa_2)
except OrderException as e:
    print(e)

try:
    krispin.buy(montar_bici)
    fake = Order(user_order, article_order, krispin, visa_2)
except OrderException as e:
    print(e)

try:
    yessi.buy(arte_insulto, 2)
    yessi.buy(braille, 4)
    yessi.buy(baston, 5)
    unavailable = Order(user_order, article_order, yessi, dinners)
except OrderException as e:
    print(e)

try:
    expired = Card(Number("4222222222222"), lucas, yesterday)
    lucas.buy(arte_insulto, 2)
    unpaid = Order(user_order, article_order, lucas, expired)
except CardException as e:
    print(e)

try:
    anonymous = Book(set(), "133", "El Necronomicón", Date("10/3/2009"), 35.00, 210, 4)
except ArticleException as e:
    print(e)

print("Total of orders: {}".format(Order.number_of_orders))
