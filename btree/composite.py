from abc import ABC
from btree.component import Component
from btree import leaf
from btree import component
class Composite(Component, ABC):
    def __init__(self,t):
        super().__init__()
        self.children = []
        self.root = Composite(True)
        self.t = t
    def findKey(self, k: int) -> bool:
        if k in self.keys:
            return True
        nextNode = self.findNextNode(k)
        return nextNode.findKey(k)

    def findNextNode(self, x: int) -> Component:
        i = 0
        while i < len(self.getKeys()) and x > self.getKeys()[i]:
            i += 1
        return self.getChildren()[i]

    def addChild(self, child: Component) -> None :
        self.children.append(child)

    def getChildren(self) -> list:
        return self.children

    def search(self, k: int, x :component =None):
        if x is not None :
            i = 0
            while (i <= x.getKeys() and k >=  x.getKeys()[i][0]):
                i+=1
            if (i <= x.getKeys() and k == x.getKeys()[i][0]):
                return (x,i)
            elif x.leaf :
                return None
            else:
                return self.search(k,x.child[i])
        else :
            return self.search(k,self.root)



