from abc import abstractmethod
from btree import leaf
from btree import composite


class Component:
    def __init__(self):
        self.keys = []

    @abstractmethod
    def check(self):
        pass

    def addKey(self, key: int) -> None:
        self.keys.append(key)

    def removeKey(self, key: int) -> None:
        self.keys.remove(key)

    def getKeys(self) -> list:
        return self.keys

    @abstractmethod
    def findKey(self, k: int) -> bool:
        pass

