
from order import Order
from twentyPercent import TwentyPercent
from fiftyPercent import FiftyPercent
from noDiscount import NoDiscount
from customDiscount import CustomDiscount

vintao = TwentyPercent()
cincao = FiftyPercent()
nada = NoDiscount()
personalizado = CustomDiscount(200)

order = Order(1000, vintao)
print(order.total, order.total_with_discount)

order = Order(1000, cincao)
print(order.total, order.total_with_discount)

order = Order(1000, nada)
print(order.total, order.total_with_discount)

order = Order(1000, personalizado)
print(order.total, order.total_with_discount)
