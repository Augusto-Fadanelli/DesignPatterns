from typing import List, Any

from binarytree import Node

from iterator_interface import Iterator

class ListIterator(Iterator):
    def __init__(self, collection: List[Any]):
        self._collection = collection
        self._index = -1

    def getNext(self):
        self._index += 1
        return self._collection[self._index]

    def hasMore(self):
        if len(self._collection) <= self._index + 1:
            return False
        return True


class TreeIterator(Iterator):
    def __init__(self, collection: Node):
        self._collection = collection
        self._temp_list = collection.values
        self._index = -1

    def getNext(self):
        self._index += 1
        return self._temp_list[self._index]

    def hasMore(self):
        if len(self._collection) <= self._index + 1:
            return False
        return True

    def getTree(self):
        return self._collection