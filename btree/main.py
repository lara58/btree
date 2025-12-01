from btree.leaf import leaf
from btree.composite import Composite

if __name__ == '__main__':
    tree = Composite()
    tree.addKey(6)

    ch1 = Composite()
    ch1.addKey(4)
    ch2 = Composite()
    ch2.addKey(10)
    ch2.addKey(14)

    tree.addChild(ch1)
    tree.addChild(ch2)

    leaf1 = Leaf()
    leaf2 = Leaf()
    leaf3 = Leaf()
    leaf4 = Leaf()
    leaf5 = Leaf()

    leaf1.addKey(2)
    leaf2.addKey(5)
    leaf3.addKey(8)
    leaf4.addKey(12)
    leaf5.addKey(16)
    leaf5.addKey(18)

    ch1.addChild(leaf1)
    ch1.addChild(leaf2)
    ch2.addChild(leaf3)
    ch2.addChild(leaf4)
    ch2.addChild(leaf5)

    print('found' if tree.findKey(8) else 'not found')
