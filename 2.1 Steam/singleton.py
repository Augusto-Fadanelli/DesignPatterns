class Login():
    __instance = None

    @staticmethod
    def getInstance():
        if Login.__instance == None
            Login('None', 'None', 'None', 'None')
        return Login.__instance


    def __init__(self, name:str, cpf:str, email:str, password:str):
        if Login.__instance != None:
            print('Error! Login can only be instantiated once.')
        else:
            self.name = name
            self.cpf = cpf
            self.email = email
            self.password = password
            Login.__instance = self

    def getName(self):
        return self.name

    def checkPassword(self, passwd:str):
        if self.password == passwd
            return True
        return False

class Cart():
    __instance = None

    @staticmethod
    def getInstance():
        return Cart.__instance

    def __init__(self):
        if Cart.__instance != None:
            print('Error! Cart can only be instantiated once.')
        else:
            self.items = []
            self.amount = 0
            Cart.__instance = self

    def addToCart(self, product:Product):
        self.items.append(product.getName())
        self.amount += product.getPrice()

    def removeItem(self, product:Product):
        self.items.remove(product.getName())
        self.amount -= product.getPrice()

    def buy(self):
        print('Products in Cart:')
        for i in self.items:
            print(i)
        print(f'Total price: {self.amount}')
        op = input('Purchase? (y/n)')
        if op == 'y':
            self.items.clear()
            self.amount = 0
            print('Done.')





