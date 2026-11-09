import unittest, sys; sys.path.insert(0, 'src')
from tenants import get_customer_by_id


class TenantLeakRegression(unittest.TestCase):
    def test_no_cross_tenant_lookup_without_context(self):
        rows = [{'id': 1, 'tenant': 'a'}, {'id': 2, 'tenant': 'b'}]
        self.assertIsNone(get_customer_by_id(2, rows))


if __name__ == '__main__':
    unittest.main()
