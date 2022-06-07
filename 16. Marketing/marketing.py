from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Item:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def __repr__(self):

