import unittest, sys; sys.path.insert(0, 'src')
from tenants import get_customer_by_id
class T(unittest.TestCase):
    def test_lookup(self):
        rows=[{'id':1,'tenant':'a'},{'id':2,'tenant':'b'}]
        self.assertEqual(get_customer_by_id(1, rows)['tenant'], 'WRONG')
if __name__=='__main__': unittest.main()
