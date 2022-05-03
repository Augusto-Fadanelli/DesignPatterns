from abc import abstractmethod
from requests import get


#main

class Menu:
    def __init__(self, moeda_inicial, valor, moeda_final) -> None:
        self.__moeda_inicial = moeda_inicial
        self.__valor = valor
        self.__moeda_final = moeda_final

    @property
    def get_moedaInicial(self):
        return self.__moeda_inicial

    @property
    def get_valor(self):
        return self.__valor

    @property
    def get_moedaFinal(self):
        return self.__moeda_final








#api

api_key = '95cb7a414c4d5c073632'

class ConverterMoeda:
    def __init__(self, api_key):
        self.url_base = "https://free.currconv.com"
        self.api_key = api_key
        self.currencies = self.get_currencies()


#Importando as moedas
    def get_currencies(self):
        endpoint = f"/api/v7/currencies?apiKey={self.api_key}"
        url = self.url_base + endpoint
        data = get(url).json()["results"]
        data = list(data.values())
        return data


#Visualizar todas as moedas que podem ser 
    def show_currencies(self):
        for currency in self.currencies:
            nome = currency.get("currencyName", "") 
            iid = currency.get("id", "")
            symbol = currency.get("currencySymbol", "")
            print(f"{iid} | {nome} | {symbol}")


#Conversão
    def transforme_currency(self, initial_currency: str, amount: float, end_currency: str):
        endpoint = f"/api/v7/convert?q={initial_currency}_{end_currency}"
        parameter = ["&compact=ultra", f"&apiKey={self.api_key}"]
        url = self.url_base + endpoint + "".join([str(parameter) for parameter in parameter])

        data = get(url).json()

        #Tratamento de erro
        if len(data) == 0:
            print("Moeda Invalida")
            return
        rate = data[f"{initial_currency}_{end_currency}"]
        try:
            amount = float(amount)
        except:
            print("Quantidade invalida")
            return
        new_value = rate * amount
        return new_value


#Adapter

class adaptando(Menu):

    @abstractmethod
    def get_moedaInicial(self):
        return super().get_moedaInicial


    @abstractmethod
    def get_valor(self):
        return super().get_valor


    @abstractmethod
    def get_moedaFinal(self):
        return super().get_moedaFinal

    def conversao(self):
        pass


class adaptandoVisualizacao(ConverterMoeda):
    def visualizarTudo(self):
        return super().show_currencies()



andre = ()
print(andre.visualizarTudo())