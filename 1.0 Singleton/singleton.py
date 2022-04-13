class Singleton():
    '''
    Docstring:
    Modelo do design pattern singleton.
    '''
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton("Default", "Default")
        return Singleton.__instance

    def __init__(self, value1: str, value2: str):
        if Singleton.__instance != None:
            print('Erro! Singleton só pode ser instanciado uma única vez.')
        else:
            self.value1 = value1
            self.value2 = value2
            Singleton.__instance = self

    def printData(self):
        print(f'value1: {self.value1}\nvalue2: {self.value2}')

if __name__ == "__main__":
    s1 = Singleton('Abacaxi', 'Melão')
    print(s1)
    s1.printData()

    s2 = Singleton.getInstance()
    print(s2)
    s2.printData()

    s3 = Singleton('Açaí', 'Uva')
    print(s3)

