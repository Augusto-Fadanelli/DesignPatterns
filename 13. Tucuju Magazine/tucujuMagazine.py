from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Publisher(ABC):
    '''
    Subject
    '''
    @abstractmethod
    def attachSubscriber(self, subscriber: Subscriber) -> None:
        pass

    @abstractmethod
    def detachSubscriber(self, subscriber: Subscriber) -> None:
        pass

    @abstractmethod
    def notifySubscribers(self) -> None:
        pass

    @abstractmethod
    def attachArticle(self, article: Article) -> None:
        pass

    @abstractmethod
    def detachArticle(self, article: Article) -> None:
        pass

    @abstractmethod
    def getArticles(self) -> List[Article]:
        pass

class Science(Publisher):
    '''
    Gênero: Ciência.
    '''
    _subscribers: List[Subscriber] = []
    _articles: List[Article] = []
    _genre = 'Science'

    def attachSubscriber(self, subscriber: Subscriber):
        # Verifica se o subscriber já existe na lista de subscribers
        for subs in self._subscribers:
            if subs == subscriber:
                print(f'Error: {subscriber.getUserName()} has already been attached.')
                return
        self._subscribers.append(subscriber)

    def detachSubscriber(self, subscriber: Subscriber):
        try:
            self._subscribers.remove(subscriber)
        except:
            print(f'Error: {subscriber.getUserName()} is not in Science subscribers.')

    def notifySubscribers(self):
        for subscriber in self._subscribers:
            subscriber.update(self)

    def attachArticle(self, article: Article):
        # Verifica se o article já existe na lista de articles
        for art in self._articles:
            if art == article:
                print(f'Error: {article.getTitle()} has already been attached.')
                return
        self._articles.append(article)
        self.notifySubscribers() # Notifica os inscritos que um novo artigo foi publicado

    def detachArticle(self, article: Article):
        try:
            self._articles.remove(article)
            self.notifySubscribers() # Notifica os inscritos que um artigo foi removido
        except:
            print(f'Error: {article.getTitle()} is not in science genre.')

    def getArticles(self):
        return self._articles

    def getGenre(self):
        return self._genre

    def debugSubscribers(self):
        print('\nScience subscribers:')
        for subscriber in self._subscribers:
            print(subscriber.getUserName())

    def debugArticles(self):
        print('\nScience articles:')
        for article in self._articles:
            print(article.getTitle())

class Policy(Publisher):
    '''
    Gênero: Política.
    '''
    _subscribers: List[Subscriber] = []
    _articles: List[Article] = []
    _genre = 'Policy'

    def attachSubscriber(self, subscriber: Subscriber):
        # Verifica se o subscriber já existe na lista de subscribers
        for subs in self._subscribers:
            if subs == subscriber:
                print(f'Error: {subscriber.getUserName()} has already been attached.')
                return
        self._subscribers.append(subscriber)

    def detachSubscriber(self, subscriber: Subscriber):
        try:
            self._subscribers.remove(subscriber)
        except:
            print(f'Error: {subscriber.getUserName()} is not in Policy subscribers.')

    def notifySubscribers(self):
        for subscriber in self._subscribers:
            subscriber.update(self)

    def attachArticle(self, article: Article):
        # Verifica se o article já existe na lista de articles
        for art in self._articles:
            if art == article:
                print(f'Error: {article.getTitle()} has already been attached.')
                return
        self._articles.append(article)
        self.notifySubscribers() # Notifica os inscritos que um novo artigo foi publicado

    def detachArticle(self, article: Article):
        try:
            self._articles.remove(article)
            self.notifySubscribers() # Notifica os inscritos que um artigo foi removido
        except:
            print(f'Error: {article.getTitle()} is not in policy genre.')

    def getArticles(self):
        return self._articles

    def getGenre(self):
        return self._genre

    def debugSubscribers(self):
        print('\nPolicy subscribers:')
        for subscriber in self._subscribers:
            print(subscriber.getUserName())

    def debugArticles(self):
        print('\nPolicy articles:')
        for article in self._articles:
            print(article.getTitle())

class Article():
    '''
    Matéria da revista.
    '''
    def __init__(self, title: str, author: str, content: str):
        self._title = title
        self._author = author
        self._content = content

    def getTitle(self):
        return self._title

    def getAuthor(self):
        return self._author

    def getContent(self):
        return self._content

class Subscriber():
    '''
    Observer
    '''
    _policy_articles: List[Article] = []
    _science_articles: List[Article] = []

    def __init__(self, user_name: str):
        self._user_name = user_name

    def getUserName(self):
        return self._user_name

    def getArticles(self):
        #return self._articles
        article_titles = []
        if len(self._policy_articles) > 0:
            for article in self._policy_articles:
                article_titles.append(article.getTitle())
        if len(self._science_articles) > 0:
            for article in self._science_articles:
                if not article.getTitle() in article_titles: # Impede que títulos repetidos sejam mostrados
                    article_titles.append(article.getTitle())

        return article_titles

    def update(self, publisher: Publisher):
        if publisher.getGenre() == 'Policy':
            self._policy_articles = publisher.getArticles()
        elif publisher.getGenre() == 'Science':
            self._science_articles = publisher.getArticles()

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


