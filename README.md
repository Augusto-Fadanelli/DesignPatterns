# Design Patterns

<img align="left" width="380" src="https://github.com/Augusto-Fadanelli/DesignPatterns/blob/main/docs/pattern-doc.jpg">

<p align="justify">Design patterns são estruturas de código abstratas para resolver problemas genéricos. Geralmente quando bem aplicados ajudam na compreensão do código, diminuição da complexidade, manutenção e gerenciamento futuro.</p>

<p align="justify">"Os padrões de projeto tornam mais fácil reutilizar projetos e arquiteturas bem sucedidas. Expressar técnicas testadas e aprovadas as torna mais acessíveis para os desenvolvedores de novos sistemas. Os padrões de projeto ajudam a escolher alternativas de projeto que tornam um sistema reutilizável e a evitar alternativas que comprometam a reutilização. Os padrões de projeto podem melhorar a documentação e a manutenção de sistemas ao fornecer uma especificação explícita de interações de classes e objetos e o seu objetivo subjacente. Em suma, ajudam um projetista a obter mais rapidamente um projeto adequado." - Padrões de Projeto (Gof)</p>

<p align="justify">Lembre-se, design patterns não são fórmulas prontas para algoritmos. São descrições de objetos e classes que precisam ser alteradas em cada contexto específico para resolver determinado problema.</p>

### Patterns Criacionais

Se preocupam em como controlar o processo de criação de instâncias de classes.

  * [Abstract Factory](https://github.com/Augusto-Fadanelli/DesignPatterns/tree/main/design_patterns/creational/Abstract%20Factory/)
    > "Fornece uma interface para criação de famílias de objetos relacionados ou dependentes sem especificar suas classes concretas." - Padrões de Projeto (Gof)

  * Builder
    > "Separa a construção de um objeto complexo da sua representação, de modo que o mesmo processo de construção possa criar diferentes representações." - Padrões de Projeto (Gof)

  * Factory Method
    > "Define uma interface para criar um objeto, mas deixa as subclasses decidirem qual classe a ser instanciada. O Factory Method permite a uma classe postergar (defer) a instanciação às subclasses." - Padrões de Projeto (Gof)

  * Prototype
    > "Especifica os tipos de objetos a serem criados usando uma instância prototípica e criar novos objetos copiando esse protótipo." - Padrões de Projeto (Gof)

  * Singleton
    > "Garante que uma classe tenha somente uma instância e fornece um ponto global de acesso para ela." - Padrões de Projeto (Gof)

### Patterns Estruturais

Utilizam da composição estática (Herança) ou composição de objetos para formar estruturas maiores.

  * Adapter
    > "Converte a interface de uma classe em outra interface esperada pelos clientes. O Adapter permite que certas classes trabalhem em conjunto, pois de outra forma seria impossível por causa de suas interfaces incompatíveis." - Padrões de Projeto (Gof)

  * Bridge
    > "Separa uma abstração da sua implementação, de modo que as duas possam variar independentemente." - Padrões de Projeto (Gof)

  * Composite
    > "Compõe objetos em estrutura de árvore para representar hierarquias do tipo partes-todo. O Composite permite que os clientes tratem objetos individuais e composições de objetos de maneira uniforme." - Padrões de Projeto (Gof)

  * Decorator
    > "Atribui responsabilidades adicionais a um objeto dinamicamente. Os decorators fornecem uma alternativa flexível a subclasses para extensão da funcionalidade." - Padrões de Projeto (Gof)

  * Facade
    > "Fornece uma interface unificada para um conjunto de interfaces em um subsistema. O Façade define uma interface de nível mais alto que torna o subsistema mais fácil de usar." - Padrões de Projeto (Gof)

  * Flyweight
    > "Usa compartilhamento para suportar grandes quantidades de objetos, de granularidade fina, de maneira eficiente." - Padrões de Projeto (Gof)

  * Proxy
    > "Fornece um objeto representante (surrogate), ou um marcador de outro objeto, para controlar o acesso ao mesmo." - Padrões de Projeto (Gof)

### Patterns Comportamentais

Descreve os padrões de comunicação entre os objetos e como as classes e objetos interagem e distribuem responsabilidades.

  * Chain of Responsibility
    > "Evita o acoplamento do remetente de uma solicitação ao seu destinatário, dando a mais de um objeto a chance de tratar a solicitação. Encadeia os objetos receptores e passa a solicitação ao longo da cadeia até que um objeto a trate." - Padrões de Projeto (Gof)

  * Command
    > "Encapsula uma solicitação como um objeto, desta forma permitindo que você parametrize clientes com diferentes solicitações, enfileire ou registre (log) solicitações e suporte operações que podem ser desfeitas." - Padrões de Projeto (Gof)

  * Interpreter
    > "Dada uma linguagem, define uma representação para sua gramática juntamente com um interpretador que usa a representação para interpretar sentenças nessa linguagem." - Padrões de Projeto (Gof)

  * Iterator
    > "Fornece uma maneira de acessar seqüencialmente os elementos de uma agregação de objetos sem expor sua representação subjacente." - Padrões de Projeto (Gof)

  * Mediator
    > "Define um objeto que encapsula a forma como um conjunto de objetos interage. O Mediator promove o acoplamento fraco ao evitar que os objetos se refiram explicitamente uns aos outros, permitindo que você varie suas interações independentemente." - Padrões de Projeto (Gof)

  * Memento
    > "Sem violar o encapsulamento, captura e externaliza um estado interno de um objeto, de modo que o mesmo possa posteriormente ser restaurado para este estado." - Padrões de Projeto (Gof)

  * Observer
    > "Define uma dependência um-para-muitos entre objetos, de modo que, quando um objeto muda de estado, todos os seus dependentes são automaticamente notificados e atualizados." - Padrões de Projeto (Gof)

  * State
    > "Permite que um objeto altere seu comportamento quando seu estado interno muda. O objeto parecerá ter mudado de classe." - Padrões de Projeto (Gof)

  * Strategy
    > "Define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis. O Strategy permite que o algoritmo varie independentemente dos clientes que o utilizam." - Padrões de Projeto (Gof)

  * Template Method
    > "Define o esqueleto de um algoritmo em uma operação, postergando a definição de alguns passos para subclasses. O Template Method permite que as subclasses redefinam certos passos de um algoritmo sem mudar sua estrutura." - Padrões de Projeto (Gof)

  * Visitor
    > "Representa uma operação a ser executada sobre os elementos da estrutura de um objeto. O Visitor permite que você defina uma nova operação sem mudar as classes dos elementos sobre os quais opera." - Padrões de Projeto (Gof)

### Referências Bibliográficas
  * Livro: Padrões de Projeto - Soluções reutilizáveis de software orientado a objetos (GoF)
  * [Refactoring Guru](https://refactoring.guru/pt-br)

#
### Rodando os Scripts em Python
  * Pré-requisitos:
    * git
    * make
    * [pyenv](https://github.com/pyenv/pyenv)
    * [pip](https://pip.pypa.io/en/stable/installation/)

  * Clonar repositório:
    ````
    $ git clone https://github.com/Augusto-Fadanelli/DesignPatterns.git
    ````

  * Instalar (Execute fora do venv):
    ````
    $ cd DesignPatterns
    $ make install
    ````

  * Para entrar/sair do ambiente virtual:
    ````
    $ source .venv/bin/activate
    $ deactivate
    ````

#
### Para desenvolvedores do Projeto
* [Standards for contributors (Portuguese)](https://github.com/Augusto-Fadanelli/DesignPatterns/tree/main/docs/Standards_for_contributors%20_pt-BR.md)
