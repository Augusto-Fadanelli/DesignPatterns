from market import Item, Cart
from chainOfResponsibility import PromotionMoreThanTenThousand, PromotionMoreThanAThousand, Promotion50Products

if __name__ == '__main__':

    # Carrinho de compras
    cart = Cart()

    # Produtos no carrinho
    # 50 itens
    for i in range(12): # Adiciona 12 bananas
        cart.addItem(Item(name='Banana', value=1.20))

    for i in range(10): # Adiciona 10 maçãs
        cart.addItem(Item(name='Maçã', value=1.50))

    for i in range(5): # Adiciona 5 kg de feijão
        cart.addItem(Item(name='Feijão', value=5.0))

    for i in range(13): # Adiciona 13 kg de arroz
        cart.addItem(Item(name='Arroz', value=4.20))

    for i in range(10): # Adiciona 10 pacotes de macarrão
        cart.addItem(Item(name='Macarrão', value=3.0))

    # 1k
    # cart.addItem(Item(name='Smartphone', value=999))

    # 10k
    # cart.addItem(Item(name='Geladeira', value=5_000))
    # cart.addItem(Item(name='Fogão', value=2_800))
    # cart.addItem(Item(name='Máquina de Lavar', value=2_200))

    # Mostra os itens no carrinho
    qtd_items = 0
    for item in cart.getItems():
        print(item)
        qtd_items += 1
    print(f'\nQuantidade total de produtos: {qtd_items}\n')

    # Mostra o valor bruto sem desconto
    print(f'Total: R${round((cart.totalValue()), 2)}')


    # Chain of Responsibility
    p_mais_de_10mil = PromotionMoreThanTenThousand()
    p_mais_de_mil = PromotionMoreThanAThousand()
    p_50produtos = Promotion50Products()

    p_mais_de_10mil.setNext(p_mais_de_mil).setNext(p_50produtos)

    print(f'Valor com desconto: R${round(p_mais_de_10mil.handle(cart), 2)}')