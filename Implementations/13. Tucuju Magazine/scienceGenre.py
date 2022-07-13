from typing import List

from observerDP import Publisher
from observerDP import Subscriber
from magazineArticles import Article

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