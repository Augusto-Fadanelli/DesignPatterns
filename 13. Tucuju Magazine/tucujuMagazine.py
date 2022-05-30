from observerDP import Subscriber
from magazineArticles import Article
from scienceGenre import Science
from policyGenre import Policy

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

    #politica.attachSubscriber(antonio)
    politica.attachSubscriber(antonio)
    politica.attachSubscriber(joao)
    politica.attachSubscriber(fernanda)

    #ciencia.debugSubscribers()
    #politica.debugSubscribers()

    #politica.detachSubscriber(antonio)
    #ciencia.detachSubscriber(joao)

    ciencia.debugSubscribers()
    politica.debugSubscribers()

    # Cria novos artigos
    artigo1 = Article(
        'Professor da UNIFAP Ganha Nobel da Paz Após Resolver Problema da Fome no Mundo',
        'William Bonner',
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum" \
        " has been the industry's standard dummy text ever since the 1500s, when an unknown" \
        " printer took a galley of type and scrambled it to make a type specimen book. It has" \
        " survived not only five centuries, but also the leap into electronic typesetting," \
        " remaining essentially unchanged. It was popularised in the 1960s with the release of" \
        " Letraset sheets containing Lorem Ipsum passages, and more recently with desktop" \
        " publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

    artigo2 = Article(
        'Artigo de Política',
        'Autor Aleatório 1',
         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum" \
        " has been the industry's standard dummy text ever since the 1500s, when an unknown" \
        " printer took a galley of type and scrambled it to make a type specimen book. It has" \
        " survived not only five centuries, but also the leap into electronic typesetting," \
        " remaining essentially unchanged. It was popularised in the 1960s with the release of" \
        " Letraset sheets containing Lorem Ipsum passages, and more recently with desktop" \
        " publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

    artigo3 = Article(
        'Artigo de Ciência',
        'Autor Aleatório 2',
         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum" \
        " has been the industry's standard dummy text ever since the 1500s, when an unknown" \
        " printer took a galley of type and scrambled it to make a type specimen book. It has" \
        " survived not only five centuries, but also the leap into electronic typesetting," \
        " remaining essentially unchanged. It was popularised in the 1960s with the release of" \
        " Letraset sheets containing Lorem Ipsum passages, and more recently with desktop" \
        " publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

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
    #print()
    #ciencia.detachArticle(artigo2) # Não está em ciencia
    #politica.detachArticle(artigo3) # Não está em politica

    # Debug: Mostra lista de artigos anexada a cada gênero
    ciencia.debugArticles()
    politica.debugArticles()

    # Mostra as novas matérias para cada inscrito
    print(f'\nAntonio:\n {antonio.getArticles()}')
    print(f'\nMaria:\n {maria.getArticles()}')
    print(f'\nJoao:\n {joao.getArticles()}')
    print(f'\nFernanda:\n {fernanda.getArticles()}')


