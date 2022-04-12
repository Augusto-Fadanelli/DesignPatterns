# DesignPatterns
  * 1.0 Singleton
  * 2.0 Bridge

# Implementações conjuntas
  * 1.2 Implementação: Singleton + Bridge

# Padrões para o desenvolvimento
  * Os design patterns serão armazenados em pastas com a sintaxe: `número na ordem em que foi pedido pelo professor`.0 `Nome do  padrão`
    * Implementações simples utilizando apenas um design pattern ficarão dentro  da pasta do design pattern em `Examples/pasta com o nome do exemplo/`
  * As implementações conjuntas serão armazenados em `Implementations` em pastas com a sintaxe: `número do design pattern utilizado`.`número do outro design pattern utilizado` `Nome da implementação`

  * Nomes de classes sempre começam com letra maiúscula
    * Se houver mais de uma palavra, a próxima plavra também começa com letra maiúscula
      * Exemplo: `ElefanteRosaVoador`
      
  * Nomes de métodos e funções sempre começam com letra minúscula
    * Se houver mais de uma palavra, as palavras seguintes começam com letra maiúscula
    * Exemplo: `elefanteRosaVoador`
  
  * Nomes de variáveis sempre começam com letra minúscula
    * Se houver mais de uma palavra, serão separadas por `_` e começarão com letra minúscula
    * Exemplo: `elefante_rosa_voador`
  
  * Classes não autodescritivas ou complexas sempre devem ter uma docstring no início explicando a finalidade, informações pertinentes e o funcionamento da mesma
    ````
    class ElefanteRosaVoador
    '''
    Docstring:
    blablabla
    '''
    def __init__(self):
    ...
    ````

  * Deve-se específicar o tipo dos parâmetros de métodos e funções, menos nos casos de o método for herdado de outra classe e na classe mãe já houver sido específicado o seu tipo
    ````
    def setNameElefante(self, name: str):
        self.name = name
    ````
    ````
    class Mae():
        def setInfo(self, nome: str, idade: int):
            self.nome = nome            
            self.idade = idade
    
    class Filha(Mae):
        def setInfo(self, nome, idade, cpf: int)
            self.nome = nome
            self.idade = idade
            self.cpf = cpf
    ````

  * Métodos abstratos que retornam um valor devem possuir uma function annotation especificando o tipo do valor retornado
    ````
    @abstractmethod
    def getElefanteRosaVoador(self) -> Elefante:
        pass
    
    @abstractmethod
    def getNameElefante(self) -> str:
        pass
    ```` 

