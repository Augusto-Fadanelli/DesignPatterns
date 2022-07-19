# Algoritmo baseado em https://youtu.be/5PRG7rT2dcU

"""
O algoritmo implementa um sistema de taxas de produtos que se alteram de acordo com o país.
"""

# from categories import *
from countryTaxes import *

if __name__ == '__main__':
    book = Book(32.5)
    food = Food(10)
    smartphone = Smartphone(1_319.99)
    computer = Computer(3_672.49)

    brazil_taxes = BRTax()
    united_state_taxes = USTax()

    cart = [book, food, smartphone, computer]

    total_price = 0
    total_price_with_taxes_brazil = 0
    total_price_with_taxes_united_states = 0
    for iten in cart:
        total_price += iten.price
        total_price_with_taxes_brazil += iten.getPriceWithTaxes(brazil_taxes)
        total_price_with_taxes_united_states += iten.getPriceWithTaxes(
            united_state_taxes
        )

    print(f'Total: {total_price}')
    print(
        f'total price with taxes Brazil: {round(total_price_with_taxes_brazil, 2)}'
    )
    print(
        f'total price with taxes United States: {round(total_price_with_taxes_united_states, 2)}'
    )
