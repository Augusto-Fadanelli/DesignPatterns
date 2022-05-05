from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass

class Leaf(Component):
    def operation(self, name='Leaf') -> str:
        return f'L:{name}'

class Composite(Component):
    def __init__(self):
        self._children: List[Component] = []

    def add(self, component: Component):
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component):
        self._children.remove(component)
        component.parent = None

    def is_composite(self):
        return True

    def operation(self, name='Branch'):
        results = []
        for child in self._children:
            results.append(child.operation())

        return f"B:{name}({' + '.join(results)})"