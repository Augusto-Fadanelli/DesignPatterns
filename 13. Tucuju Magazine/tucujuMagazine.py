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

    def debug(self):
        print('\nScience:')
        for subscriber in self._subscribers:
            print(subscriber.getUserName())

class Policy(Publisher):
    '''
    Gênero: Política.
    '''
    _subscribers: List[Subscriber] = []
    _articles: List[Article] = []

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

    def debug(self):
        print('\nPolicy:')
        for subscriber in self._subscribers:
            print(subscriber.getUserName())

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
    _articles: List[Article] = []

    def __init__(self, user_name: str):
        self._user_name = user_name

    def getUserName(self):
        return self._user_name

    def update(self, publisher: Publisher):
        self._articles = publisher.getArticles()

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

    politica.attachSubscriber(antonio)
    politica.attachSubscriber(antonio)
    politica.attachSubscriber(joao)
    politica.attachSubscriber(fernanda)

    ciencia.debug()
    politica.debug()

    politica.detachSubscriber(antonio)
    ciencia.detachSubscriber(joao)

    ciencia.debug()
    politica.debug()


