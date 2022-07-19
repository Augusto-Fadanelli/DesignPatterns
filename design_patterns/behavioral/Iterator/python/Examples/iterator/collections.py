# pip install BinaryTree

from random import randint
from typing import Any, List

from binarytree import Node, build
from collection_interface import IterableCollection
from iterator_interface import Iterator
from iterators import ListIterator, TreeIterator


class ListCollection(IterableCollection):
    def __init__(self):
        self._collection: List[Any] = []

    def createIterator(self) -> Iterator:
        return ListIterator(self._collection)

    def addItem(self, item):
        self._collection.append(item)


class TreeCollection(IterableCollection):
    def __init__(self):
        self._collection: List[Any] = []

    def createIterator(self) -> Iterator:
        return TreeIterator(build(self._collection))

    def addItem(self, item):
        self._collection.append(item)


if __name__ == '__main__':
    words_list = ListCollection()
    words_list.addItem('Primeiro')
    words_list.addItem('Segundo')
    words_list.addItem('Terceiro')

    wl_iterator = words_list.createIterator()
    while wl_iterator.hasMore():
        print(wl_iterator.getNext())
        print()

    print('=' * 15)
    print()

    numbers_tree = TreeCollection()
    numbers_tree.addItem(randint(1, 99))
    numbers_tree.addItem(randint(1, 99))
    numbers_tree.addItem(randint(1, 99))
    numbers_tree.addItem(randint(1, 99))
    numbers_tree.addItem(randint(1, 99))

    nt_iterator = numbers_tree.createIterator()

    while nt_iterator.hasMore():
        print(nt_iterator.getNext())
        print()

    print(nt_iterator.getTree())
