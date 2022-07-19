# Standards for contributors
  * O projeto segue os padrões da [pep-8](https://peps.python.org/pep-0008/) e [pep-257](https://peps.python.org/pep-0257/)

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
    $ make dev_install
    ````

  * Para entrar/sair do ambiente virtual:
    ````
    $ source .venv/bin/activate
    $ deactivate
    ````

  * Configurar pre-commit
    * Criar arquivo e dar permissão de execução
      ````
      $ touch .git/hooks/pre-commit
      $ chmod +x .git/hooks/pre-commit
      ````

    * Edite o arquivo `.git/hooks/pre-commit`
      ````
      IFS=
      pip_out=$(pip list -o 2> /dev/null)

      if [ $(echo $pip_out | wc -l) -ge 1 ]; then
          echo "Existem pacotes desatualizados (pip list -o):"
          echo $pip_out
      fi

      safety_out=$(safety check -r requirements.txt --full-report)
      safety_filter=$($safety_out |& grep "Affected" | wc -l)

      if [ $safety_filter -ge 1 ]; then
          echo "Commit não efetuado, vulnerabilidade encontrada"
          echo $safety_out
          exit 1
      fi

      make lint
      make test
      ````

  * Verifica se o código está formatado corretamente
    ````
    $ make lint
    ````

  * Testa o código
    ````
    $ make test
    ````

  * Verifica problemas de segurança relacionados aos pacotes em requirements.txt
    ````
    $ make sec
    ````

  * Formata os códigos automáticamente de acordo com a [pep-8](https://peps.python.org/pep-0008/) e [pep-257](https://peps.python.org/pep-0257/)
    ````
    $ make format
    ````

# Formatação Manual 
  * Deve-se específicar o tipo dos parâmetros de métodos e funções, menos nos casos de o método for herdado de outra classe e na superclasse já houver sido específicado o seu tipo
    ````
    def square(self, number: int):
        return number * number
    ````
    ````
    class Animal():
        def setInfo(self, name: str, age: int):
            pass

    class Bird(Animal):
        def setInfo(self, name, age, weight: float)
            pass
    ````

  * Métodos abstratos que retornam um valor devem possuir uma function annotation especificando o tipo do valor retornado
    ````
    @abstractmethod
    def square(self, number: int) -> int:
        return number * number
    ````
