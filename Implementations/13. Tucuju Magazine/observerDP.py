from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from magazineArticles import Article


class Publisher(ABC):
    """
    Subject
    """

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


class Subscriber:
    """
    Observer
    """

    _policy_articles: List[Article] = []
    _science_articles: List[Article] = []

    def __init__(self, user_name: str):
        self._user_name = user_name

    def getUserName(self):
        return self._user_name

    def getArticles(self):
        # return self._articles
        article_titles = []
        if len(self._policy_articles) > 0:
            for article in self._policy_articles:
                article_titles.append(article.getTitle())
        if len(self._science_articles) > 0:
            for article in self._science_articles:
                if (
                    not article.getTitle() in article_titles
                ):   # Impede que títulos repetidos sejam mostrados
                    article_titles.append(article.getTitle())

        return article_titles

    def update(self, publisher: Publisher):
        if publisher.getGenre() == 'Policy':
            self._policy_articles = publisher.getArticles()
        elif publisher.getGenre() == 'Science':
            self._science_articles = publisher.getArticles()
