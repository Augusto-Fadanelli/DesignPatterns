from magazineArticles import Article
from observerDP import Subscriber
from policyGenre import Policy
from scienceGenre import Science

if __name__ == '__main__':
    # Client code

    ciencia = Science()
    politica = Policy()

    antonio = Subscriber('Antonio')
    joao = Subscriber('João')
    maria = Subscriber('Maria')
    fernanda = Subscriber('Fernanda')

    ciencia.attachSubscriber(antonio)
    ciencia.attachSubscriber(maria)

    # politica.attachSubscriber(antonio)
    politica.attachSubscriber(antonio)
    politica.attachSubscriber(joao)
    politica.attachSubscriber(fernanda)

    # ciencia.debugSubscribers()
    # politica.debugSubscribers()

    # politica.detachSubscriber(antonio)
    # ciencia.detachSubscriber(joao)

    ciencia.debugSubscribers()
    politica.debugSubscribers()

    # Cria novos artigos
    artigo1 = Article(
        'Professor da UNIFAP Ganha Nobel da Paz Após Resolver Problema da Fome no Mundo',
        'William Bonner',
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum'
        " has been the industry's standard dummy text ever since the 1500s, when an unknown"
        ' printer took a galley of type and scrambled it to make a type specimen book. It has'
        ' survived not only five centuries, but also the leap into electronic typesetting,'
        ' remaining essentially unchanged. It was popularised in the 1960s with the release of'
        ' Letraset sheets containing Lorem Ipsum passages, and more recently with desktop'
        ' publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
    )

    artigo2 = Article(
        'Governo bloqueia verba para custeio e investimento de universidades federais',
        'Ana Paula Castro',
        'O Ministério da Educação bloqueou nesta sexta-feira (27) 14,5 por cento da verba das '
        'universidades e institutos federais para despesas de custeio e investimento. O governo '
        'diz que o contingenciamento é necessário para cumprir o teto de gastos, regra que '
        'limita o crescimento das despesas públicas. O bloqueio feito em 2022 deve ser maior '
        'que o previsto, no entanto, porque o Executivo tenta encaixar nesse limite a promessa '
        'de dar reajuste aos servidores públicos federais. Ao todo, R$ 14 bilhões devem ser '
        'bloqueados em todo o governo federal para garantir um reajuste de 5 por cento em ano '
        ' eleitoral. No documento enviado às universidades, ao qual a TV Globo teve acesso, o '
        'MEC diz que sofreu um bloqueio de R$ 3,23 bilhões, equivalente a 14,5 por cento de '
        'toda a verba de uso discricionário para este ano. E que decidiu repassar esse '
        'percentual de forma linear (uniforme) a todas as unidades e órgãos vinculados ao '
        'ministério – ou seja, bloquear 14,5 por cento de cada universidade, instituto ou '
        ' entidade ligada ao MEC.',
    )

    artigo3 = Article(
        'As Auroras Marcianas São Finalmente Explicadas',
        'Sergio Sacani',
        'O Planeta Vermelho é famoso por ter perdido o seu campo magnético global, e nós '
        'aprendemos desde sempre que as auroras só acontecem devido a interação das partículas '
        'carregadas do Sol com o campo magnético do planeta, então como isso pode ser possível '
        'em Marte? Embora Marte não tenha campo magnético global não quer dizer que o planeta '
        'seja totalmente livre de magnetismo. Existem regiões de campo magnético localizado em '
        'pontos específicos da crosta, principalmente no hemisfério sul. Novas análises '
        'confirmaram que esses pequenos campos magnéticos localizados interagem com o vento '
        'solar de maneira interessante, de modo a produzir auroras em Marte. Mas são auroras '
        'que só são visíveis no ultravioleta. Mas em Marte não temos esse campo magnético, o que'
        ' temos são manchas de magnetismo preservadas em minerais que estão magnetizados ainda '
        'na crosta do planeta. Imagens em ultravioleta de Marte, mostram que as auroras tendem '
        'a se formar perto desses campos magnéticos remanescentes, o que faz sentido se as '
        'linhas de campo magnético forem necessárias para a aceleração das partículas.',
    )

    # Anexa artigos ao seu gênero
    ciencia.attachArticle(artigo1)
    politica.attachArticle(artigo1)

    politica.attachArticle(artigo2)

    ciencia.attachArticle(artigo3)

    # Debug: Mostra lista de artigos anexada a cada gênero
    ciencia.debugArticles()
    politica.debugArticles()

    # Mostra as novas matérias para cada inscrito
    print(f'\nAntonio:\n {antonio.getArticles()}')
    print(f'\nMaria:\n {maria.getArticles()}')
    print(f'\nJoao:\n {joao.getArticles()}')
    print(f'\nFernanda:\n {fernanda.getArticles()}')

    # Remove artigos
    ciencia.detachArticle(artigo1)
    politica.detachArticle(artigo1)

    # Remove errado
    # print()
    # ciencia.detachArticle(artigo2) # Não está em ciencia
    # politica.detachArticle(artigo3) # Não está em politica

    # Debug: Mostra lista de artigos anexada a cada gênero
    ciencia.debugArticles()
    politica.debugArticles()

    # Mostra as novas matérias para cada inscrito
    print(f'\nAntonio:\n {antonio.getArticles()}')
    print(f'\nMaria:\n {maria.getArticles()}')
    print(f'\nJoao:\n {joao.getArticles()}')
    print(f'\nFernanda:\n {fernanda.getArticles()}')
