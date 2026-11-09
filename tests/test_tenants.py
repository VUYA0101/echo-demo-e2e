import unittest, sys; sys.path.insert(0, 'src')
from tenants import get_customer_by_id
class T(unittest.TestCase):
    def test_lookup(self):
        rows=[{'id':1,'tenant':'a'},{'id':2,'tenant':'b'}]
        self.assertEqual(get_customer_by_id(1, rows, tenant_id='a')['tenant'], 'a')

    def test_foreign_tenant_returns_none(self):
        rows=[{'id':1,'tenant':'a'},{'id':2,'tenant':'b'}]
        self.assertIsNone(get_customer_by_id(2, rows, tenant_id='a'))

    def test_missing_tenant_context_returns_none(self):
        rows=[{'id':1,'tenant':'a'}]
        self.assertIsNone(get_customer_by_id(1, rows))
        self.assertIsNone(get_customer_by_id(1, rows, tenant_id=None))

    def test_same_id_in_both_tenants(self):
        rows=[{'id':1,'tenant':'a','n':'A'},{'id':1,'tenant':'b','n':'B'}]
        self.assertEqual(get_customer_by_id(1, rows, tenant_id='a')['n'], 'A')
        self.assertEqual(get_customer_by_id(1, rows, tenant_id='b')['n'], 'B')

    def test_swapped_row_order(self):
        rows=[{'id':1,'tenant':'b','n':'B'},{'id':1,'tenant':'a','n':'A'},{'id':2,'tenant':'b'}]
        self.assertEqual(get_customer_by_id(1, rows, tenant_id='a')['n'], 'A')
        self.assertIsNone(get_customer_by_id(2, list(reversed(rows)), tenant_id='a'))
if __name__=='__main__': unittest.main()
