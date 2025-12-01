from asyncio.windows_events import NULL
import unittest
from btree.component import component
from btree.composite import composite
class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_getKeys(self):
        c = component()
        self.assertEquals(c.getKeys(),NULL)
        c.addKey(9)
        c.addKey(4)
        c.addKey(7)
        self.assertEquals(c.getKeys(),[4,7,9])      
if __name__ == '__main__':
    unittest.main()