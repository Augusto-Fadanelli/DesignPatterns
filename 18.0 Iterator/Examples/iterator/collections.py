# pip install BinaryTree

from typing import List, Any
from random import randint

from binarytree import Node, build

from iterator_interface import Iterator
from collection_interface import IterableCollection
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
    if wl_iterator.hasMore():
        print(wl_iterator.getNext())
        print()
    else:
        print('fim')

    if wl_iterator.hasMore():
        print(wl_iterator.getNext())
        print()
    else:
        print('fim')

    if wl_iterator.hasMore():
        print(wl_iterator.getNext())
        print()
    else:
        print('fim')

    if wl_iterator.hasMore():
        print(wl_iterator.getNext())
        print()
    else:
        print('fim')

    print()
    print('='*15)
    print()

    numbers_tree = TreeCollection()
    numbers_tree.addItem(randint(1, 99))
    numbers_tree.addItem(randint(1, 99))
    numbers_tree.addItem(randint(1, 99))
    numbers_tree.addItem(randint(1, 99))
    numbers_tree.addItem(randint(1, 99))

    nt_iterator = numbers_tree.createIterator()

    if nt_iterator.hasMore():
        print(nt_iterator.getNext())
        print()
    else:
        print('fim')

    if nt_iterator.hasMore():
        print(nt_iterator.getNext())
        print()
    else:
        print('fim')

    if nt_iterator.hasMore():
        print(nt_iterator.getNext())
        print()
    else:
        print('fim')

    if nt_iterator.hasMore():
        print(nt_iterator.getNext())
        print()
    else:
        print('fim')

    if nt_iterator.hasMore():
        print(nt_iterator.getNext())
        print()
    else:
        print('fim')

    if nt_iterator.hasMore():
        print(nt_iterator.getNext())
        print()
    else:
        print('fim')

    print(nt_iterator.getTree())