from discountStrategy import DiscountStrategy


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value
