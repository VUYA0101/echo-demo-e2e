import unittest, sys; sys.path.insert(0, 'src')
from tenants import get_customer_by_id
class T(unittest.TestCase):
    def test_lookup(self):
        rows=[{'id':1,'tenant':'a'},{'id':2,'tenant':'b'}]
        self.assertEqual(get_customer_by_id(1, rows, tenant_id='a')['tenant'], 'a')
    def test_foreign_tenant_is_not_found(self):
        rows=[{'id':1,'tenant':'a'},{'id':2,'tenant':'b'}]
        self.assertIsNone(get_customer_by_id(2, rows, tenant_id='a'))
    def test_same_id_in_both_tenants_any_order(self):
        rows=[{'id':1,'tenant':'b'},{'id':1,'tenant':'a'}]
        self.assertEqual(get_customer_by_id(1, rows, tenant_id='a')['tenant'], 'a')
        self.assertEqual(get_customer_by_id(1, list(reversed(rows)), tenant_id='b')['tenant'], 'b')
    def test_missing_tenant_context_denies_access(self):
        rows=[{'id':1,'tenant':'a'},{'id':2,'tenant':'b'}]
        self.assertIsNone(get_customer_by_id(1, rows, tenant_id=None))
if __name__=='__main__': unittest.main()
