from abc import ABC

from btree.component import Component


class Leaf(Component, ABC):

    def __init__(self):
        super().__init__()

    def findKey(self, k: int):
        return k in self.getKeys()