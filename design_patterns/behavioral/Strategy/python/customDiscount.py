from discountStrategy import DiscountStrategy


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount: float) -> None:
        self._discount = discount / 100

    # def checker(self, valueChecker) -> None:
    #    if self._discount < 100:
    #        valueChecker = self._discount
    #    print("O desconto deve ser menor que 100")

    def calculate(self, value: float) -> float:
        return value - (value * self._discount)
