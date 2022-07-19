class Article:
    """
    Matéria da revista.
    """

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
